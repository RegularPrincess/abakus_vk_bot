#!/usr/bin/env python3
## -*- coding: utf-8 -*-
#Кнопки

BTN_ENROLL = "Записаться на бесплатное занятие"
BTN_CANCEL = "⛔ Отмена"
BTN_BROADCAST = "Рассылка"
BTN_ADD_ADMIN = "Добавить администратора"
BTN_ADMINS = "Администраторы"
BTN_SUBS = "Подписчики"
BTN_MENU = "Меню пользователя"


START_WORDS = ['start', 'начать', 'старт']
USER_ACCEPT_WORDS = ['да', 'конечно', 'хочу']

#Сообщения для пользователя
MSG_WELCOME_TO_COURSE = 'Приветствуем, {!s}!🖐 Вы хотите записаться на бесплатное занятие?'
MSG_ACCEPT_NAME = 'Напишите, пожалуйста, Как к Вам обращаться?'
MSG_ACCEPT_EMAIL = 'Введите, пожалуйста, адрес Вашей електронной почты (email) 📧'
MSG_ACCEPT_NUMBER = 'Введите, пожалуйста, Ваш номер телефона ☎'
MSG_ENROLL_COMPLETED = 'Спасибо, {}! ' \
                       'Мы очень ценим, что Вы выбрали нас! В ближайшее время наш сотрудник свяжется с Вами!'
MSG_CANCELED_MESSAGE = 'Действие успешно отменено.'
MSG_DEFAULT_ANSWER = 'Ничего не понятно('
MSG_PLEASE_STAND_BY = 'Это может занять некоторое время...'
MSG_MEMBERS_COUNT = 'Пользователей в группе - {0}'
MSG_ADDED_COUNT = 'Из них еще не было в базе и было добавлено - {0}'
MSG_UNCORECT_NUMBER = '❗ Данный формат номера телефона не распознан! \n' \
                      'Пожалуйста введите в формате +7 321 123456789, либо 8 (код города) 111 11 11'
MSG_UNCORECT_EMAIL = '❗ Адрес электронной почты не распознан. Введите, пожалуйста, в формате example@domain.ru'
MSG_SUBS = '🔥 ПОДПИСЧИКИ БОТА 🔥'


#Статусы подписчиков
USER_LEAVE_STATUS = 'leave'
USER_SUB_STATUS = 'member'
USER_RETURN_STATUS = 'return'
USER_NOT_SUB_STATUS = 'notmember'

#Сообщения для администраторов
NOTIFY_ADMIN = 'Пользователь с id{} записался на бесплатное занятие. \n\n' \
               'Его данные: \n🖐 обращение - {},\n📧 email - {},\n☎ номер телефона - {}.'
ADMIN_KEY_WORDS = ['admin', 'админ']
MSG_YOU_NOT_ADMIN = 'Вы не являйтесь администратором.'
MSG_ADMIN_EXIT = 'Выйти из меню администратора'
MSG_ACCEPT_BROADCAST = '🖊 Введите сообщение для рассылки:'
MSG_BROADCAST_COMPLETED = 'Сообщение разослано {} пользователям.'
MSG_ADMIN_REMOVING = '🐩 Для удаления администратора введите его номер ID'
MSG_VALUE_ERROR = 'Не корректно! Введите только цифры id.'
MSG_ADMIN_REMOVED = 'Администратор успешно удален!'
CMD_PARSE_GROUP = 'parsegroup'
MSG_ADMIN_ADDING = '🔥 ДОБАВИТЬ АДМИНИСТРАТОРА: 🔥\n\n' \
                   '🔑 ВВЕДИТЕ id НОВОГО АДМИНИСТРАТОРА БОТА. \n' \
                   'id – ЭТО ЧИСЛОВОЕ ЗНАЧЕНИЕ ПОСЛЕ https://vk.com/id.\n\n'\
                   '👉 НАПРИМЕР: В СЛУЧАЕ ПОЛНОГО id: https://vk.com/id12345678 ' \
                   'НЕОБХОДИМО ВВЕСТИ: 12345678'
MSG_ADMIN_SUCCCES_ADDED = "Администратор успешно добавлен"
MSG_SERVER_RESTARTED = 'Сервер перезапущен'
MSG_ADMINS = '🔥 СПИСОК АДМИНИСТРАТОРОВ: 🔥 \n\n'
MSG_USER_SHORT_INFO = '👉 Количество участников в группе: {} \n' \
                      '👍 Из них рассылка возможна {} участникам'

MSG_GROUP_JOIN = '''
Приветствуем, {!s}! 
'''

GROUP_LEAVE_MESSAGE = '''
Ждем тебя снова!
'''

#Клавиатуры
EMPTY_KEYBOARD = ''

KEYBOARD_USER = {
                "one_time": False,
                "buttons": [
                    [{
                        "action": {
                        "type": "text",
                            "payload": "{\"button\": \"1\"}",
                            "label": BTN_ENROLL
                        },
                        "color": "positive"
                    }],
                ]
            }


KEYBOARD_CANCEL = {
                "one_time": False,
                "buttons": [
                    [{
                        "action": {
                        "type": "text",
                            "payload": "{\"button\": \"1\"}",
                            "label": BTN_CANCEL
                        },
                        "color": "default"
                    }]
                ]
            }


MSG_ADMIN_PANEL = '''🔥 ПАНЕЛЬ АДМИНИСТРАТОРА 🔥'''

KEYBOARD_ADMIN = {
    "one_time": False,
    "buttons": [
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"1\"}",
          "label": BTN_BROADCAST
        },
        "color": "default"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"2\"}",
          "label": BTN_SUBS
        },
        "color": "default"
      }],
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"3\"}",
          "label": BTN_ADMINS
        },
        "color": "default"
      },
     {
        "action": {
          "type": "text",
          "payload": "{\"button\": \"4\"}",
          "label": BTN_ADD_ADMIN
        },
        "color": "default"
      }],
      [{
        "action": {
          "type": "text",
          "payload": "{\"button\": \"5\"}",
          "label": MSG_ADMIN_EXIT
        },
        "color": "default"
      }]
    ]
  }

