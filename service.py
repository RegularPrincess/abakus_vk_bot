#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import model as m
import consts as cnst
import vklib as vk
import db_utils as db


READY_TO_ENROLL = {}


def group_join(uid):
    uname = vk.get_user_name(uid)
    if uname == '':
        uname = 'No Name'
    db.add_bot_follower(uid, uname)
    vk.send_message_keyboard(uid, cnst.WELCOME_TO_COURSE.format(uname), cnst.user_enroll_keyboard)
    return 'ok'


def del_uid_from_dict(uid, dict_):
    if uid in dict_:
        del dict_[uid]


def send_message_admins(info):
    admins = db.get_list_bot_admins()
    vk.send_message_much(admins, cnst.NOTIFY_ADMIN.format(info.uid, info.name, info.email, info.number))


def message_processing(uid, text):
    uname = vk.get_user_name(uid)
    if text.lower() in cnst.START_WORDS:
        vk.send_message_keyboard(uid, cnst.WELCOME_TO_COURSE.format(uname), cnst.user_enroll_keyboard)
    elif text == cnst.ENROLL:
        READY_TO_ENROLL[uid] = m.Enroll_info(uid)
        vk.send_message_keyboard(uid, cnst.ACCEPT_NAME, cnst.user_cancel_keyboard)
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
    return 'ok'


def group_leave(uid):
    uname = vk.get_user_name(uid)
    db.set_bot_follower_status(uid, cnst.USER_LEAVE_STATUS)
    vk.send_message_keyboard(uid, cnst.GROUP_LEAVE_MESSAGE.format(uname), cnst.EMPTY_KEYBOARD)
    return 'ok'
