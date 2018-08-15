import json
import os
import re

import datetime

import copy
import requests

import utils.vklib as vk
import utils.db_utils as db
import model as m
import consts as cnst
import config as cfg


def make_subs_file(uid):
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


def del_uid_from_dict(uid, dict_):
    if uid in dict_:
        del dict_[uid]


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


def new_user_or_not(uid, uname):
    e = db.is_known_user(uid)
    if e or db.is_admin(uid):
        if e:
            db.set_bot_follower_mess_allowed(uid, 1)
    else:
        db.add_bot_follower(uid, uname, status=cnst.USER_NOT_SUB_STATUS, msg_allowed=1)
        vk.send_message_keyboard(uid, cnst.MSG_WELCOME_TO_COURSE.format(uname), cnst.KEYBOARD_USER)


def parse_bcst(text):
    try:
        obj = m.BcstByTime()
        text_arr = text.split(' ', maxsplit=3)
        obj.start_date = datetime.datetime.strptime(text_arr[0], '%d.%m.%Y').date()
        obj.time = datetime.datetime.strptime(text_arr[1], '%H:%M').time()
        obj.repet_days = int(text_arr[2])
        return obj
    except BaseException:
        return None


def get_leave_reasons_as_str():
    reasons_list = db.get_leave_reasons()
    reasons_str = ''
    for r in reasons_list:
        reasons_str += r + '\n'
    return reasons_str


def save_leave_reasons(reasons_str):
    reasons = reasons_str.split('; ', 8)
    for r in reasons:
        db.add_leave_reason(r)
    return len(reasons)


def get_keyboard_from_list(list):
    keyboard = copy.deepcopy(cnst.keyboard_pattern.copy())
    c = 0
    for i in list:
        if c == 7:
            break
        one_btns = copy.deepcopy(cnst.one_button_pattern)
        one_btns[0]['action']['label'] = i
        j = {"button": 'K'}
        one_btns[0]['action']['payload'] = json.dumps(j)
        keyboard['buttons'].append(one_btns)
        c += 1
    keyboard['buttons'].append(cnst.enroll_btn)
    return keyboard


def send_data_to_uon(data, uid):
    today = datetime.datetime.today()
    t = today.time()
    date_str = '{} {}:{}:{}'.format(today.date(), t.hour, t.minute, t.second)
    note = 'Куда: {}\nКто: {}\nКогда: {}\nБюджет на человека: {}\n '.\
        format(data.where, data.who, data.when, data.budget)
    payload = {
        'r_dat': date_str,
        'u_name': data.name,
        'source': 'Бот вконтакте',
        'u_phone': data.number,
        'u_email': data.email,
        'u_social_vk': ('id' + uid),
        'u_note': note
    }

    url = 'https://api.u-on.ru/6COVU66eHPjf667alVq3/lead/create.json'
    response = requests.post(url, data=payload)
    print(response)