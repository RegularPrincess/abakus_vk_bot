#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import re
import requests

import model as m
import consts as cnst
import vklib as vk
import db_utils as db
import config as cfg


READY_TO_ENROLL = {}
IN_ADMIN_PANEL = {}


def admin_message_processing(uid, uname, text):
    if text == cnst.MSG_ADMIN_EXIT:
        del_uid_from_dict(uid, IN_ADMIN_PANEL)
        vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)

    elif text == cnst.BTN_BROADCAST:
        IN_ADMIN_PANEL[uid] = cnst.BTN_BROADCAST
        all_count = vk.get_count_group_followers(cfg.group_id)
        msg_allowed_count = db.get_msg_allowed_count()
        vk.send_message(uid, cnst.MSG_USER_SHORT_INFO.format(all_count, msg_allowed_count))
        vk.send_message_keyboard(uid, cnst.MSG_ACCEPT_BROADCAST, cnst.KEYBOARD_CANCEL)

    elif text == cnst.BTN_SUBS:
        vk.send_message(uid, cnst.MSG_PLEASE_STAND_BY)
        vk_doc_link = make_subs_file(uid)
        vk.send_message_doc(uid, '', vk_doc_link)

    elif text == cnst.BTN_ADMINS:
        IN_ADMIN_PANEL[uid] = cnst.BTN_ADMINS
        admins = db.get_bot_admins()
        msg = 'Администраторы: \n\n'
        for a in admins:
            msg += '{}, id - {}\n\n'.format(a.name, a.uid)
        msg += cnst.MSG_ADMIN_REMOVING
        vk.send_message_keyboard(uid, msg, cnst.KEYBOARD_CANCEL)

    elif text == cnst.BTN_ADD_ADMIN:
        IN_ADMIN_PANEL[uid] = cnst.BTN_ADD_ADMIN
        vk.send_message_keyboard(uid, cnst.MSG_ADMIN_ADDING, cnst.KEYBOARD_CANCEL)

    elif text.lower() == cnst.CMD_PARSE_GROUP:
        if db.is_admin(uid):
            members_count = get_group_count()
            msg = cnst.MSG_MEMBERS_COUNT.format(members_count)
            vk.send_message(uid, msg)
            vk.send_message(uid, cnst.MSG_PLEASE_STAND_BY)
            added_count = parse_group(members_count)
            msg = cnst.MSG_ADDED_COUNT.format(added_count)
            vk.send_message(uid, msg)
        else:
            vk.send_message_keyboard(uid, cnst.MSG_YOU_NOT_ADMIN, cnst.KEYBOARD_USER)
    elif text == cnst.BTN_CANCEL:
        IN_ADMIN_PANEL[uid] = ''
        vk.send_message_keyboard(uid, cnst.MSG_CANCELED_MESSAGE, cnst.KEYBOARD_ADMIN)

    elif IN_ADMIN_PANEL[uid] == cnst.BTN_BROADCAST:
        count = db.vk_emailing_to_all_subs(text)
        vk.send_message_keyboard(uid, cnst.MSG_BROADCAST_COMPLETED.format(count), cnst.KEYBOARD_ADMIN)
        IN_ADMIN_PANEL[uid] = ''

    elif IN_ADMIN_PANEL[uid] == cnst.BTN_ADMINS:
        try:
            admin_id = int(text)
            db.delete_admin(admin_id)
            msg = cnst.MSG_ADMIN_REMOVED
            vk.send_message_keyboard(uid, msg, cnst.KEYBOARD_ADMIN)
            IN_ADMIN_PANEL[uid] = ''
        except ValueError:
            msg = cnst.MSG_VALUE_ERROR
            vk.send_message(uid, msg)

    elif IN_ADMIN_PANEL[uid] == cnst.BTN_ADD_ADMIN:
        try:
            admin_id = int(text)
            name = vk.get_user_name(admin_id)
            db.add_bot_admin(admin_id, name)
            vk.send_message_keyboard(uid, cnst.MSG_ADMIN_SUCCCES_ADDED, cnst.KEYBOARD_ADMIN)
            IN_ADMIN_PANEL[uid] = ''
        except ValueError:
            msg = cnst.MSG_VALUE_ERROR
            vk.send_message(uid, msg)
    else:
        vk.send_message(uid, cnst.MSG_DEFAULT_ANSWER)


def message_processing(uid, text):
    uname = vk.get_user_name(uid)
    if uid in IN_ADMIN_PANEL:
        admin_message_processing(uid, uname, text)
        return 'ok'

    if text.lower() in cnst.START_WORDS:
        vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)

    elif text == cnst.BTN_ENROLL or (text.lower() in cnst.USER_ACCEPT_WORDS and not_ready_to_enroll(uid)):
        READY_TO_ENROLL[uid] = m.Enroll_info(uid)
        vk.send_message_keyboard(uid, cnst.MSG_ACCEPT_NAME, cnst.KEYBOARD_CANCEL)

    elif text == cnst.BTN_CANCEL:
        del_uid_from_dict(uid, READY_TO_ENROLL)
        vk.send_message_keyboard(uid, cnst.MSG_CANCELED_MESSAGE, cnst.KEYBOARD_USER)

    # Обработка ввода данных пользователя
    elif uid in READY_TO_ENROLL:
        if not READY_TO_ENROLL[uid].name_is_sign():
            READY_TO_ENROLL[uid].set_name(text)
            vk.send_message(uid, cnst.MSG_ACCEPT_EMAIL)
        elif not READY_TO_ENROLL[uid].email_is_sign():
            if is_email_valid(text):
                READY_TO_ENROLL[uid].set_email(text)
                vk.send_message(uid, cnst.MSG_ACCEPT_NUMBER)
            else:
                vk.send_message(uid, cnst.MSG_UNCORECT_EMAIL)
        elif not READY_TO_ENROLL[uid].number_is_sign():
            if is_number_valid(text):
                READY_TO_ENROLL[uid].set_number(text)
                send_message_admins(READY_TO_ENROLL[uid])
                del_uid_from_dict(uid, READY_TO_ENROLL)
                vk.send_message_keyboard(uid, cnst.MSG_ENROLL_COMPLETED, cnst.KEYBOARD_USER)
            else:
                vk.send_message(uid, cnst.MSG_UNCORECT_NUMBER)

    # Вход для админа
    elif text.lower() in cnst.ADMIN_KEY_WORDS and not_ready_to_enroll(uid):
        if db.is_admin(uid):
            IN_ADMIN_PANEL[uid] = ''
            vk.send_message_keyboard(uid, cnst.MSG_ADMIN_PANEL, cnst.KEYBOARD_ADMIN)
        else:
            vk.send_message_keyboard(uid, cnst.MSG_YOU_NOT_ADMIN, cnst.KEYBOARD_USER)
    else:
        vk.send_message(uid, cnst.MSG_DEFAULT_ANSWER)
    return 'ok'


def group_leave(uid):
    uname = vk.get_user_name(uid)
    db.set_bot_follower_status(uid, cnst.USER_LEAVE_STATUS)
    vk.send_message_keyboard(uid, cnst.GROUP_LEAVE_MESSAGE.format(uname), cnst.EMPTY_KEYBOARD)
    return 'ok'


def make_subs_file(uid):
    db.update_mess_allowed_info()
    bot_followers = db.get_bot_followers()
    if len(bot_followers) == 0:
        text = 'В боте ещё нет подписчиков'
        vk.send_message(uid, text)
        return 'ok'
    filename = 'subs.csv'
    out = open(filename, 'a')
    text = 'ID; Имя; Статус; Подписан на рассылку\n'
    out.write(text)
    for x in bot_followers:
        text = '{};{};{};{}\n'.format(x.uid, x.name, x.status, x.mess_allowed)
        out.write(text)
    out.close()
    res = vk.get_doc_upload_server1(uid)
    print(res)
    upload_url = res['response']['upload_url']
    files = {'file': open(filename, 'r')}
    response = requests.post(upload_url, files=files)
    result = response.json()
    print(result)
    r = vk.save_doc(result['file'])
    vk_doc_link = 'doc{!s}_{!s}'.format(r['response'][0]['owner_id'], r['response'][0]['id'])
    print(vk_doc_link)
    os.remove(filename)
    return vk_doc_link


def get_group_count(group_id=cfg.group_id):
    members_count = vk.get_count_group_followers(group_id)
    return int(members_count)


def parse_group(members_count, group_id=cfg.group_id):
    follower_list = db.get_bot_followers(only_id=True)
    iterations = members_count // 1000 + 1
    users_added = 0
    for x in range(iterations):
        users = vk.get_group_memebers(group_id, offset=x * 1000, count=1000)
        for user_id in users:
            try:
                if not user_id in follower_list:
                    username = vk.get_user_name(user_id)
                    msg_allowed = 0
                    if vk.is_messages_allowed(user_id):
                        msg_allowed = 1
                    db.add_bot_follower(user_id, username, msg_allowed=msg_allowed)
                    users_added += 1
            except Exception as e:
                pass
    return users_added


def group_join(uid):
    uname = vk.get_user_name(uid)
    if uname == '':
        uname = 'No Name'
    msg_allowed = 0
    if vk.is_messages_allowed(uid):
        msg_allowed = 1
    db.add_bot_follower(uid, uname, msg_allowed=msg_allowed)
    vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)
    return 'ok'


def del_uid_from_dict(uid, dict_):
    if uid in dict_:
        del dict_[uid]


def not_ready_to_enroll(uid):
    return uid not in READY_TO_ENROLL


def send_message_admins(info):
    admins = db.get_list_bot_admins()
    vk.send_message_much(admins, cnst.NOTIFY_ADMIN.format(info.uid, info.name, info.email, info.number))


def send_message_admins_after_restart():
    admins = db.get_list_bot_admins()
    vk.send_message_much_keyboard(admins, cnst.MSG_SERVER_RESTARTED, cnst.KEYBOARD_USER)


def is_number_valid(number):
    match = re.fullmatch('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,9}', number)
    if match:
        return True
    else:
        return False


def is_email_valid(email):
    match = re.fullmatch('[\w.-]+@\w+\.\w+', email)
    if match:
        return True
    else:
        return False
