#!/usr/bin/env python3
## -*- coding: utf-8 -*-
#Кнопки

ENROLL = "Записаться на беспоатное занятие"
CANCEL = "⛔ Отмена"

BROADCAST = "Рассылка"
ADD_ADMIN = "Добавить администратора"
ADMINS = "Администраторы"
SUBS = "Подписчики"
MENU = "Меню пользователя"


START_WORDS = ['start', 'начать', 'старт']
USER_ACCEPT_WORDS = ['да', 'конечно', 'хочу']

WELCOME_TO_COURSE = 'Приветствуем, {!s}! Вы хотите записаться на бесплатное занятие?'
ACCEPT_NAME = 'Как к Вам обращаться?'
ACCEPT_EMAIL = 'Введите Ваш email.'
ACCEPT_NUMBER = 'Введите Ваш номер телефона.'
ENROLL_COMPLETED = 'Мы всё записали и в ближайшее время с Вами свяжется наш администратор!'
CANCELED_MESSAGE = 'Действие успешно отменено.'
DEFAULT_ANSWER = 'Ничего не понятно('
PLEASE_WAIT = 'Это может занять некоторое время...'

USER_LEAVE_STATUS = 'leave'
USER_SUB_STATUS = 'member'
USER_RETURN_STATUS = 'return'

NOTIFY_ADMIN = 'Пользователь с id{} записался на бесплатное занятие. ' \
               'Его данные: обращение - {}, email - {}, номер телефона - {}.'
ADMIN_KEY_WORDS = ['admin', 'админ']
YOU_NOT_ADMIN = 'Вы не являйтесь администратором.'
ADMIN_EXIT = 'Выйти из меню администратора'
ACCEPT_BROADCAST = 'Введите сообщение для рассылки:'
BROADCAST_COMPLETED = 'Сообщение разослано {} пользователям.'
ADMIN_REMOVING = 'Для удаления администратора отправте его целочисленный id.'
VALUE_ERROR = 'Не корректно! Введите только цифры id.'
ADMIN_REMOVED = 'Администратор {} успешно удален!'

group_join_text = '''
Приветствуем, {!s}! 
'''

GROUP_LEAVE_MESSAGE = '''
Ждем тебя снова!
'''


EMPTY_KEYBOARD = ''

user_enroll_keyboard = {
                "one_time": False,
                "buttons": [
                    [{
                        "action": {
                        "type": "text",
                            "payload": "{\"button\": \"1\"}",
                            "label": ENROLL
                        },
                        "color": "positive"
                    }],
                ]
            }


cancel_keyboard = {
                "one_time": False,
                "buttons": [
                    [{
                        "action": {
                        "type": "text",
                            "payload": "{\"button\": \"1\"}",
                            "label": CANCEL
                        },
                        "color": "default"
                    }]
                ]
            }


admin_panel_text = '''🔥 ПАНЕЛЬ АДМИНИСТРАТОРА 🔥'''

admin_menu_keyboard = {
    "one_time": False,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": BROADCAST
        },
        "color": "default"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": SUBS
        },
        "color": "default"
      }],
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"3\"}",
          "label": ADMINS
        },
        "color": "default"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"4\"}",
          "label": ADD_ADMIN
        },
        "color": "default"
      }],
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"5\"}",
          "label": ADMIN_EXIT
        },
        "color": "default"
      }]
    ]
  }

