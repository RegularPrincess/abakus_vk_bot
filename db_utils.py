#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlite3 import dbapi2 as sqlite3

import vklib
import config
import model as m
import consts as cnst


with sqlite3.connect(config.db_name) as connection:
    cursor = connection.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS known_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        uid INTEGER UNIQUE NOT NULL,
        status TEXT NOT NULL,
        name TEXT NOT NULL,
        written_on_course INTEGER DEFAULT 0,
        mess_allowed INTEGER DEFAULT 0)'''
    cursor.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        uid INTEGER UNIQUE NOT NULL,
        name TEXT NOT NULL)'''
    cursor.execute(sql)
    # Add base admins to bot
    sql = '''INSERT OR IGNORE INTO admins (uid, name) VALUES ({!s}, '{!s}')'''.format(
        config.admin_id, config.admin_name)
    cursor.execute(sql)
    connection.commit()


def update_mess_allowed_info():
    uids = get_bot_followers(only_id=True)
    for uid in uids:
        if vklib.is_messages_allowed(uid):
            set_bot_follower_mess_allowed(uid, 1)
        else:
            set_bot_follower_mess_allowed(uid, 0)


def vk_emailing_to_all_subs(text):
    """
    Разослать текст всем подписчикам, кому возможно группы
    """
    count = 0
    arr = []
    users = get_bot_followers()
    for u in users:
        if u.is_msging_allowed():
            arr.append(u)
            count += 1
        if len(arr) == 100:
            vklib.send_message_much(arr, text)
            arr = []
    vklib.send_message_much(arr, text)
    return count


def get_bot_admins():
    """
    Получить админов бота
    """
    arr = []
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''SELECT * FROM admins'''
        res = cursor.execute(sql).fetchall()
        print(res)
        for x in res:
            arr.append(m.Admin(x[1], x[2]))
        connection.commit()
    return arr


def get_list_bot_admins():
    """
    Получить админов бота как список
    """
    arr = []
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''SELECT * FROM admins'''
        res = cursor.execute(sql).fetchall()
        print(res)
        for x in res:
            arr.append(x[1])
        connection.commit()
    return arr


def is_admin(uid):
    admins = get_list_bot_admins()
    return uid in admins


def delete_admin(admin_id):
    """
    Удалить админа
    """
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''DELETE FROM admins WHERE uid=?'''
        cursor.execute(sql, (admin_id,))
        connection.commit()


def add_bot_admin(uid, name):
    """
    Добавить админа бота
    """
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''INSERT OR IGNORE INTO admins (uid, name) VALUES (?, ?)'''
        cursor.execute(sql, (uid, name))
        connection.commit()


def set_bot_follower_status(uid, status):
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''UPDATE known_users SET status=? WHERE uid=?'''
        cursor.execute(sql, (status, uid))
        connection.commit()


def set_bot_follower_mess_allowed(uid, status):
    """
    status = 0 or 1
    """
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''UPDATE known_users SET mess_allowed=? WHERE uid=?'''
        cursor.execute(sql, (status, uid))
        connection.commit()


def add_bot_follower(uid, name, status=cnst.USER_SUB_STATUS, msg_allowed=0):
    """
    Добавить подписчика бота
    """
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''INSERT OR IGNORE INTO known_users (uid, status, name, mess_allowed) VALUES (?, ?, ?, ?)'''
        cursor.execute(sql, (uid, status, name, msg_allowed))
        connection.commit()


def get_bot_followers(only_id=False):
    """
    Получить подписчиков бота
    """
    arr = []
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''SELECT * FROM known_users'''
        res = cursor.execute(sql).fetchall()
        print(res)
        for x in res:
            item = x[1] if only_id else m.Follower(x[1], x[3], x[2], x[4], x[5])
            arr.append(item)
        connection.commit()
    return arr
