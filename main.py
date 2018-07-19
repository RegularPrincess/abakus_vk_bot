#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import json

import service as s
import config

token = config.token
confirmation_token = config.confirmation_token
secret_key = config.secret_key
group_id = config.group_id
admin_id = config.admin_id
admin_name = config.admin_name
db_name = config.db_name
bot_name = config.bot_name
vk_api_url = config.vk_api_url


app = Flask(__name__)


@app.route(rule='/', methods=['GET'])
def debug():
    return "hello world"


@app.route(rule='/{0}'.format(bot_name), methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'secret' not in data.keys():
        return 'Not VK.'
    elif not data['secret'] == secret_key:
        return 'Bad query.'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'group_join':
        uid = data['object']['user_id']
        answer = s.group_join(uid)
        return answer
    elif data['type'] == 'message_new':
        uid = data['object']['from_id']
        text = data['object']['text']
        answer = s.message_processing(uid, text)
        return answer
    elif data['type'] == 'group_leave':
        uid = data['object']['user_id']
        answer = s.group_leave(uid)
        return answer


def main(argv):
    #port = int(argv[0])
    app.run(host='0.0.0.0', port=8088, debug=True)

if __name__ == '__main__':
    import sys
    main(sys.argv[0:])
