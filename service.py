#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import requests

import model as m
import consts as cnst
import vklib as vk
import db_utils as db
import config as cfg


READY_TO_ENROLL = {}
IN_ADMIN_PANEL = {}


def group_join(uid):
    uname = vk.get_user_name(uid)
    if uname == '':
        uname = 'No Name'
    msg_allowed = 0
    if vk.is_messages_allowed(uid):
        msg_allowed = 1
    db.add_bot_follower(uid, uname, msg_allowed=msg_allowed)
    vk.send_message_keyboard(uid, cnst.WELCOME_TO_COURSE.format(uname), cnst.user_enroll_keyboard)
    return 'ok'


def del_uid_from_dict(uid, dict_):
    if uid in dict_:
        del dict_[uid]


def not_ready_to_enroll(uid):
    return uid not in READY_TO_ENROLL


def send_message_admins(info):
    admins = db.get_list_bot_admins()
    vk.send_message_much(admins, cnst.NOTIFY_ADMIN.format(info.uid, info.name, info.email, info.number))


def admin_message_processing(uid, uname, text):
    if text == cnst.ADMIN_EXIT:
        del_uid_from_dict(uid, IN_ADMIN_PANEL)
        vk.send_message_keyboard(uid, cnst.WELCOME_TO_COURSE.format(uname), cnst.user_enroll_keyboard)
    elif text == cnst.BROADCAST:
        IN_ADMIN_PANEL[uid] = cnst.BROADCAST
        vk.send_message_keyboard(uid, cnst.ACCEPT_BROADCAST, cnst.cancel_keyboard)
    elif text == cnst.SUBS:
        vk.send_message(uid, cnst.PLEASE_WAIT)
        vk_doc_link = make_subs_file(uid)
        vk.send_message_doc(uid, '', vk_doc_link)
    elif text == cnst.ADMINS:
        IN_ADMIN_PANEL[uid] = cnst.ADMINS
        admins = db.get_bot_admins()
        msg = 'Администраторы: \n\n'
        for a in admins:
            msg += '{}, id - {}\n\n'.format(a.name, a.uid)
        msg += cnst.ADMIN_REMOVING
        vk.send_message_keyboard(uid, msg, cnst.cancel_keyboard)
    elif text == cnst.ADD_ADMIN:
        IN_ADMIN_PANEL[uid] = cnst.ADD_ADMIN
        vk.send_message_keyboard(uid, cnst.ADMIN_ADDING, cnst.cancel_keyboard)
    elif text.lower() == cnst.PARSE_GROUP:
        if db.is_admin(uid):
            members_count = get_group_count()
            msg = cnst.MEMBERS_COUNT.format(members_count)
            vk.send_message(uid, msg)
            vk.send_message(uid, cnst.PLEASE_WAIT)
            added_count = parse_group(members_count)
            msg = cnst.ADDED_COUNT.format(added_count)
            vk.send_message(uid, msg)
        else:
            vk.send_message_keyboard(uid, cnst.YOU_NOT_ADMIN, cnst.user_enroll_keyboard)
    elif text == cnst.CANCEL:
        IN_ADMIN_PANEL[uid] = ''
        vk.send_message_keyboard(uid, cnst.CANCELED_MESSAGE, cnst.admin_menu_keyboard)
    elif IN_ADMIN_PANEL[uid] == cnst.BROADCAST:
        count = db.vk_emailing_to_all_subs(text)
        vk.send_message(uid, cnst.BROADCAST_COMPLETED.format(count))
        IN_ADMIN_PANEL[uid] = ''
    elif IN_ADMIN_PANEL[uid] == cnst.ADMINS:
        try:
            admin_id = int(text)
            db.delete_admin(admin_id)
            msg = cnst.ADMIN_REMOVED
            vk.send_message_keyboard(uid, msg, cnst.admin_menu_keyboard)
            IN_ADMIN_PANEL[uid] = ''
        except ValueError:
            msg = cnst.VALUE_ERROR
            vk.send_message(uid, msg)
    elif IN_ADMIN_PANEL[uid] == cnst.ADD_ADMIN:
        try:
            admin_id = int(text)
            name = vk.get_user_name(admin_id)
            db.add_bot_admin(admin_id, name)
            vk.send_message_keyboard(uid, cnst.ADMIN_SUCCCES_ADDED, cnst.admin_menu_keyboard)
            IN_ADMIN_PANEL[uid] = ''
        except ValueError:
            msg = cnst.VALUE_ERROR
            vk.send_message(uid, msg)
    else:
        vk.send_message(uid, cnst.DEFAULT_ANSWER)


def message_processing(uid, text):
    uname = vk.get_user_name(uid)
    if uid in IN_ADMIN_PANEL:
        admin_message_processing(uid, uname, text)
        return 'ok'

    if text.lower() in cnst.START_WORDS:
        vk.send_message_keyboard(uid, cnst.WELCOME_TO_COURSE.format(uname), cnst.user_enroll_keyboard)

    elif text == cnst.ENROLL or (text.lower() in cnst.USER_ACCEPT_WORDS and not_ready_to_enroll(uid)):
        READY_TO_ENROLL[uid] = m.Enroll_info(uid)
        vk.send_message_keyboard(uid, cnst.ACCEPT_NAME, cnst.cancel_keyboard)

    elif text == cnst.CANCEL:
        del_uid_from_dict(uid, READY_TO_ENROLL)
        vk.send_message_keyboard(uid, cnst.CANCELED_MESSAGE, cnst.user_enroll_keyboard)

    # Обработка ввода данных пользователя
    elif uid in READY_TO_ENROLL:
        if not READY_TO_ENROLL[uid].name_is_sign():
            READY_TO_ENROLL[uid].set_name(text)
            vk.send_message(uid, cnst.ACCEPT_EMAIL)
        elif not READY_TO_ENROLL[uid].email_is_sign():
            READY_TO_ENROLL[uid].set_email(text)
            vk.send_message(uid, cnst.ACCEPT_NUMBER)
        elif not READY_TO_ENROLL[uid].number_is_sign():
            READY_TO_ENROLL[uid].set_number(text)
            send_message_admins(READY_TO_ENROLL[uid])
            del_uid_from_dict(uid, READY_TO_ENROLL)
            vk.send_message_keyboard(uid, cnst.ENROLL_COMPLETED, cnst.user_enroll_keyboard)

    # Вход для админа
    elif text in cnst.ADMIN_KEY_WORDS and not_ready_to_enroll(uid):
        if db.is_admin(uid):
            IN_ADMIN_PANEL[uid] = ''
            vk.send_message_keyboard(uid, cnst.admin_panel_text, cnst.admin_menu_keyboard)
        else:
            vk.send_message_keyboard(uid, cnst.YOU_NOT_ADMIN, cnst.user_enroll_keyboard)
    else:
        vk.send_message(uid, cnst.DEFAULT_ANSWER)
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
