#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

import requests
import utils.vklib as vk

import config as cfg
import consts as cnst
import model as m
from utils import db_utils as db
from utils import service_utils as utils

READY_TO_ENROLL = {}
IN_ADMIN_PANEL = {}

utils.send_message_admins_after_restart()


def admin_message_processing(uid, uname, text):
    if text == cnst.MSG_ADMIN_EXIT:
        utils.del_uid_from_dict(uid, IN_ADMIN_PANEL)
        vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)

    elif text == cnst.BTN_BROADCAST:
        IN_ADMIN_PANEL[uid] = cnst.BTN_BROADCAST
        all_count = vk.get_count_group_followers(cfg.group_id)
        msg_allowed_count = db.get_msg_allowed_count()
        vk.send_message(uid, cnst.MSG_USER_SHORT_INFO.format(all_count, msg_allowed_count))
        vk.send_message_keyboard(uid, cnst.MSG_ACCEPT_BROADCAST, cnst.KEYBOARD_CANCEL)

    elif text == cnst.BTN_SUBS:
        vk.send_message(uid, cnst.MSG_PLEASE_STAND_BY)
        vk_doc_link = utils.make_subs_file(uid)
        vk.send_message_doc(uid, cnst.MSG_SUBS, vk_doc_link)

    elif text == cnst.BTN_ADMINS:
        IN_ADMIN_PANEL[uid] = cnst.BTN_ADMINS
        admins = db.get_bot_admins()
        msg = cnst.MSG_ADMINS
        for a in admins:
            msg += '🔑 {}, id - {}\n\n'.format(a.name, a.uid)
        msg += cnst.MSG_ADMIN_REMOVING
        vk.send_message_keyboard(uid, msg, cnst.KEYBOARD_CANCEL)

    elif text == cnst.BTN_ADD_ADMIN:
        IN_ADMIN_PANEL[uid] = cnst.BTN_ADD_ADMIN
        vk.send_message_keyboard(uid, cnst.MSG_ADMIN_ADDING, cnst.KEYBOARD_CANCEL)

    elif text.lower() == cnst.CMD_PARSE_GROUP:
        if db.is_admin(uid):
            members_count = utils.get_group_count()
            msg = cnst.MSG_MEMBERS_COUNT.format(members_count)
            vk.send_message(uid, msg)
            vk.send_message(uid, cnst.MSG_PLEASE_STAND_BY)
            added_count = utils.parse_group(members_count)
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
        pass
        # vk.send_message(uid, cnst.MSG_DEFAULT_ANSWER)


def message_processing(uid, text):
    uname = vk.get_user_name(uid)
    if uid in IN_ADMIN_PANEL:
        admin_message_processing(uid, uname, text)
        return 'ok'

    if text.lower() in cnst.START_WORDS:
        vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)
        utils.new_user_or_not(uid, uname)

    elif text == cnst.BTN_ENROLL or (text.lower() in cnst.USER_ACCEPT_WORDS and not_ready_to_enroll(uid)):
        READY_TO_ENROLL[uid] = m.EnrollInfo(uid)
        vk.send_message_keyboard(uid, cnst.MSG_ACCEPT_NAME, cnst.KEYBOARD_CANCEL)
        utils.new_user_or_not(uid, uname)

    elif text == cnst.BTN_CANCEL:
        utils.del_uid_from_dict(uid, READY_TO_ENROLL)
        vk.send_message_keyboard(uid, cnst.MSG_CANCELED_MESSAGE, cnst.KEYBOARD_USER)

    # Обработка ввода данных пользователя
    elif uid in READY_TO_ENROLL:
        if not READY_TO_ENROLL[uid].name_is_sign():
            READY_TO_ENROLL[uid].set_name(text)
            vk.send_message(uid, cnst.MSG_ACCEPT_EMAIL)
        elif not READY_TO_ENROLL[uid].email_is_sign():
            if utils.is_email_valid(text):
                READY_TO_ENROLL[uid].set_email(text)
                vk.send_message(uid, cnst.MSG_ACCEPT_NUMBER)
            else:
                vk.send_message(uid, cnst.MSG_UNCORECT_EMAIL)
        elif not READY_TO_ENROLL[uid].number_is_sign():
            if utils.is_number_valid(text):
                READY_TO_ENROLL[uid].set_number(text)
                vk.send_message_keyboard(uid, cnst.MSG_ENROLL_COMPLETED.format(READY_TO_ENROLL[uid].name), cnst.KEYBOARD_USER)
                utils.send_message_admins(READY_TO_ENROLL[uid])
                utils.del_uid_from_dict(uid, READY_TO_ENROLL)
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
        utils.new_user_or_not(uid, uname)
        # vk.send_message(uid, cnst.MSG_DEFAULT_ANSWER)
    return 'ok'


def not_ready_to_enroll(uid):
    return uid not in READY_TO_ENROLL


def group_leave(uid):
    uname = vk.get_user_name(uid)
    vk.send_message_keyboard(uid, cnst.GROUP_LEAVE_MESSAGE.format(uname), cnst.EMPTY_KEYBOARD)
    db.set_bot_follower_status(uid, cnst.USER_LEAVE_STATUS)
    utils.del_uid_from_dict(uid, IN_ADMIN_PANEL)
    utils.del_uid_from_dict(uid, READY_TO_ENROLL)
    return 'ok'


def group_join(uid):
    uname = vk.get_user_name(uid)
    if uname == '':
        uname = 'No Name'
    msg_allowed = 0
    if vk.is_messages_allowed(uid):
        msg_allowed = 1
    if db.is_known_user(uid):
        db.set_bot_follower_status(uid, cnst.USER_SUB_STATUS)
    else:
        db.add_bot_follower(uid, uname,  msg_allowed=msg_allowed)
    vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)
    utils.del_uid_from_dict(uid, IN_ADMIN_PANEL)
    utils.del_uid_from_dict(uid, READY_TO_ENROLL)
    return 'ok'


def message_allow(uid):
    db.set_bot_follower_mess_allowed(uid, 1)
    uname = vk.get_user_name(uid)
    vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)
    utils.new_user_or_not(uid, uname)
    return 'ok'


def message_deny(uid):
    db.set_bot_follower_mess_allowed(uid, 0)
    return 'ok'
