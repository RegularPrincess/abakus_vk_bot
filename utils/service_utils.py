import os
import re
import requests

import utils.vklib as vk
import utils.db_utils as db
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

