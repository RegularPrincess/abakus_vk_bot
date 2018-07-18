#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import requests

from flask import Flask
from flask import request
from flask import json

import util
import vklib
import config
import consts as c

token = config.token
confirmation_token = config.confirmation_token
secret_key = config.secret_key
group_id = config.group_id
admin_id = config.admin_id
admin_name = config.admin_name
db_name = config.db_name
bot_name = config.bot_name

vk_api_url = config.vk_api_url

READY_TO_EMAILING = []
READY_TO_ADD_NEW_ADMIN = {}
READY_TO_ADD_NEW_PRODUCT = {}
READY_TO_ADD_NEW_CATEGORY = {}
READY_TO_DOSTAVKA = {}
READY_TO_EDIT_CATEGORY = {}
READY_TO_EDIT_PRODUCT = {}
READY_TO_ADD_BASKET = {}

PRODUCT_LIST = []
PRODUCT_CATEG_LIST = []
CATEGORY_LIST = []

LAST_COMMAND = {}
CANCEL = {}

app = Flask(__name__)


with sqlite3.connect(db_name) as connection:
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
        admin_id, admin_name)
    cursor.execute(sql)
    connection.commit()


@app.route(rule='/', methods=['GET'])
def debug():
    return "hello world"


@app.route(rule='/{0}'.format(bot_name), methods=['POST'])
def processing():

    f = open('log', 'a')
    f.write("processing start \n")
    f.close()

    data = json.loads(request.data)

    f = open('log', 'a')
    f.write("processing start " + data['type'] + '\n')
    f.close()

    if 'secret' not in data.keys():
        return 'Not VK.'
    elif not data['secret'] == secret_key:
        return 'Bad query.'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'group_join':
        uname = vklib.get_user_name(data['object']['user_id'])
        if uname == '':
            uname = 'No Name'
        util.add_bot_follower(data['object']['user_id'], uname)
        vklib.send_message_keyboard(data['object']['user_id'], c.group_join_text.format(uname), c.user_menu_keyboard)
        return 'ok'


def main(argv):

    f = open('log', 'w')
    f.write("Start\n")
    f.close()

    #port = int(argv[0])
    app.run(host='0.0.0.0', port=8088, debug=True)

if __name__ == '__main__':
    import sys
    main(sys.argv[0:])
