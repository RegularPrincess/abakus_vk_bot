#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlite3 import dbapi2 as sqlite3

import vklib
import config


with sqlite3.connect(config.db_name) as connection:
    cursor = connection.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS known_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        uid INTEGER UNIQUE NOT NULL,
        status TEXT NOT NULL,
        name TEXT NOT NULL)'''
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


class Admin:
    def __init__(self, uid, name, status='member'):
        self.uid = uid
        self.name = name
        # self.status = status


class Follower:
    def __init__(self, uid, name, status='member'):
        self.uid = uid
        self.name = name
        self.status = status


def vk_emailing(users, text):
    """
    Разослать текст всем подписчикам группы
    """
    arr = []
    for uid in users:
        arr.append(uid)
        if len(arr) == 100:
            vklib.send_message_much(arr, text)
            arr = []
    vklib.send_message_much(arr, text)


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
            arr.append(Admin(x[1], x[2]))
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


def add_bot_follower(uid, name, status="member"):
    """
    Добавить подписчика бота
    """
    with sqlite3.connect(config.db_name) as connection:
        cursor = connection.cursor()
        sql = '''INSERT OR IGNORE INTO known_users (uid, status, name) VALUES (?, ?, ?)'''
        cursor.execute(sql, (uid, status, name))
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
            item = x[1] if only_id else Follower(x[1], x[3],x[2])
            arr.append(item)
        connection.commit()
    return arr
