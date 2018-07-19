## -*- coding: utf-8 -*-
#Кнопки

ENROLL = "📝 Записаться"
CANCEL = "⛔ Отмена"

BROADCAST = "Рассылка"
ADD_ADMIN = "Добавить администратора"
ADMINS = "Администраторы"
SUBS = "Подписчики"
MENU = "Меню пользователя"


START_WORDS = ['start', 'начать', 'старт']
USER_ACCEPT_WORDS = ['да', 'конечно', 'хочу']

WELCOME_TO_COURSE = 'Приветствуем, {!s}!. Вы хотите записаться на бесплатное занятие?'
ACCEPT_NAME = 'Как к Вам обращаться?'
ACCEPT_EMAIL = 'Введите Ваш email.'
ACCEPT_NUMBER = 'Введите Ваш номер телефона.'
ENROLL_COMPLETED = 'Мы всё записали и в ближайшее время с Вами свяжется наш администратор!'

CANCELED_MESSAGE = 'Действие успешно отменено.'

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
                        "color": "default"
                    }],
                ]
            }


user_cancel_keyboard = {
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


admin_panel_text = '''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
||||||||||||||||||||||||| 🔥 ПАНЕЛЬ АДМИНИСТРАТОРА 🔥 |||||||||||||||||||||||||| 
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
'''

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
                            "label": ADD_GOODS
                        },
                        "color": "default"
                    }],


                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"3\"}",
                            "label": ADD_CAT
                        },
                        "color": "default"
                    }],


                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"4\"}",
                            "label": EDIT_CAT
                        },
                        "color": "default"
                    },
                    {
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"5\"}",
                            "label": EDIT_GOODS
                        },
                        "color": "default"
                    }],


                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"6\"}",
                            "label": ADD_ADMIN
                        },
                        "color": "default"
                    },
                    {
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"7\"}",
                            "label": ADMINS
                        },
                        "color": "default"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"8\"}",
                            "label": SUBS
                        },
                        "color": "default"
                    },
                    {
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"9\"}",
                            "label": MENU
                        },
                        "color": "default"
                    }]
                ]
            }

