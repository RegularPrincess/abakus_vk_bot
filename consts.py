#!/usr/bin/env python3
## -*- coding: utf-8 -*-

SEPARATOR = '|'

# Кнопки
BTN_ENROLL = "Записаться на бесплатное занятие"
BTN_CANCEL = "⛔ Отмена"
BTN_BROADCAST = "Рассылка"
BTN_ADD_ADMIN = "Добавить администратора"
BTN_ADMINS = "Администраторы"
BTN_SUBS = "Подписчики"
BTN_MENU = "Меню пользователя"
BTN_ADD_BROADCAST_BY_TIME = 'Создать рассылку по расписанию'
BTN_BROADCAST_BY_TIME = 'Запланированные рассылки'
BTN_LEAVE_REASON = 'Причины отписки'
BTN_ADRESSES = 'Адреса офисов'
BTN_END = 'Закончить'
BTN_EDIT_YEAR = 'Изменить возраста'

DEF_YEARS = "4-5; 6-8; 9-11; 12-14; 14-16"

START_WORDS = ['start', 'начать', 'старт']
USER_ACCEPT_WORDS = ['да', 'конечно', 'хочу', 'да.']

# Сообщения для пользователя
MSG_WELCOME_TO_COURSE = 'Приветствуем, {!s}!🖐 Вы хотите записаться на бесплатное занятие?'
MSG_ACCEPT_NAME = 'Напишите, пожалуйста, как к Вам обращаться?'
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
MSG_ACCEPT_ADRESS = 'Выберите адресс офиса. 👉 Перешлите в ответном сообщении необходимый адрес.'
MSG_LEAVING = '😢 Сообщите, пожалуйса, причину по которой вы покидайте нашу группу' \
              ' или выберите вариант из предложенного списка.'
MSG_THANK_YOU = 'Спасибо!'
MSG_SUBS = '🔥 ПОДПИСЧИКИ БОТА 🔥'
MSG_ADRESSES_ = 'Адреса офисов: '
MSG_ADRESSES_CHANGE = '👉 Для удаления отправте id офиса, для добавления нового - ' \
                      'введите название города и следуйте дальнейшим инструкциям.'
# 'ПРИМЕР: Красной Позиции, 2А, Казань'
MSG_ADRESSES_REMOVED = 'Адрес успешно удален.'
SHOOSE_ADDRESS = "Выберите адрес офиса из предложенных."

# Статусы подписчиков
USER_LEAVE_STATUS = 'leave'
USER_SUB_STATUS = 'member'
USER_RETURN_STATUS = 'return'
USER_NOT_SUB_STATUS = 'notmember'

# Сообщения для администраторов
NOTIFY_ADMIN = 'Пользователь с id{} записался на бесплатное занятие. \n\n' \
               'Его данные: \n🖐 обращение - {},\n☎ номер телефона - {}. \nВозраст - {},\n' \
               '👉 Выбран офис по адресу: {}'
ADMIN_KEY_WORDS = ['admin', 'админ']
MSG_YOU_NOT_ADMIN = 'Вы не являйтесь администратором.'
BTN_ADMIN_EXIT = 'Выйти из меню администратора'
MSG_ACCEPT_BROADCAST = '🖊 Введите сообщение для рассылки:'
MSG_BROADCAST_COMPLETED = 'Сообщение разослано {} пользователям.'
MSG_ADMIN_REMOVING = '🐩 Для удаления администратора введите его номер ID'
MSG_VALUE_ERROR = 'Не корректно! Введите только цифры id.'
MSG_ADMIN_REMOVED = 'Администратор успешно удален!'
CMD_PARSE_GROUP = 'parsegroup'
MSG_ADMIN_ADDING = '🔥 ДОБАВИТЬ АДМИНИСТРАТОРА: 🔥\n\n' \
                   '🔑 ВВЕДИТЕ id НОВОГО АДМИНИСТРАТОРА БОТА. \n' \
                   'id – ЭТО ЧИСЛОВОЕ ЗНАЧЕНИЕ ПОСЛЕ https://vk.com/id.\n\n' \
                   '👉 НАПРИМЕР: В СЛУЧАЕ ПОЛНОГО id: https://vk.com/id12345678 ' \
                   'НЕОБХОДИМО ВВЕСТИ: 12345678'
MSG_ADMIN_SUCCCES_ADDED = "Администратор успешно добавлен"
MSG_SERVER_RESTARTED = 'Сервер перезапущен'
MSG_ADMINS = '🔥 СПИСОК АДМИНИСТРАТОРОВ: 🔥 \n\n'
MSG_USER_SHORT_INFO = '👉 Количество участников в группе: {} \n' \
                      '👍 Рассылка возможна {} участникам'
MSG_ADD_BRDCST_BY_TIME = "👉 Введите дату с которой следует начать рассылку, " \
                         "затем время рассылки(мск), " \
                         "затем количество дней через котрое рассылка будет повторена.\n\n" \
                         "👉 Пример: 22.08.2018 15:22 3"
MSG_PLANNED_BCST = 'Дата начала - {}, время - {}, периодичность повторений (дней) - {}, id - {}\n' \
                   '🖊 Сообщение - {} \n\n'
MSG_USER_LEAVED = 'Пользоваетль {} id{} покинул группу, указав причину: \"{}\"'
MSG_LAST_MSG = '👉 Текущее сообщенеи при записи пользователя: \n' \
               '"{}" \n\n🖊 Вы можете заменить его отправив новое.' \
               'Для обращения к пользователю используйте символы - {}\n\n' \
               '👉 ПРИМЕР: "Спасибо, {}! Мы очень ценим, что Вы выбрали нас!"'
MSG_GROUP_JOIN = '''
Приветствуем, {!s}!
'''
GROUP_LEAVE_MESSAGE = '''
Ждем тебя снова!
'''
MSG_LEAVE_REASON = "👉 Текущие возможные причины: \n\n {} " \
                   "\n\n🖊 Вы можете заменить эти причины, " \
                   "отправив новые, разделенные точкой с запятой (до 7 вариантов)\n\n" \
                   "👉 ПРИМЕР: Просто так; Надоела рассылка; Тема больше не интересна"
MSG_LEAVE_REASON_SAVED = "Причины отписки успешно сохранены (старые удалены). Количество - {}."
# MSG_LEAVE_REASON_NOT_SAVED = "Причины не указаны"
MSG_ADRESS_INFO = "ID-{}; {} \n {}"
MSG_ADRESS_ERROR = 'Не корректный адрес!'
MSG_ADRESS_SAVED = 'Адрес успешно сохранен.'
MSG_END = 'Действие завершено'
MSG_END_ADDING_ADRESS_OR_NOT = \
    'Вы можете добавить ссылку на связанный с офисом ресурс или можете завершить процедуру.'
MSG_ADDING_MORE_ADRESS_OR_NOT = "Вы можете добавить еще ссылку или завершить."
BTN_LAST_MSG = 'Сообщения пользователю'
SAVED = 'Сохранено!'
MSG_EDIT_YEARS = "Текущие варианты возраста: {}\n\nОтправте новые для замены в таком же формате."
SHOOSE_YEAR = "Выберите возраст записываемого на занятие."

# Клавиатуры
EMPTY_KEYBOARD = ''

one_button_pattern = [{
    "action": {
        "type": "text",
        "payload": "{\"button\": \"3\"}",
        "label": ""
    },
    "color": "default"
}]

cancel_btn = [{
    "action": {
        "type": "text",
        "payload": "{\"button\": \"1\"}",
        "label": BTN_CANCEL
    },
    "color": "default"
}]

enroll_btn = [{
    "action": {
        "type": "text",
        "payload": "{\"button\": \"1\"}",
        "label": BTN_ENROLL
    },
    "color": "positive"
}]

keyboard_pattern = \
    {
        "one_time": False,
        "buttons": []
    }

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

KEYBOARD_CANCEL_AND_YEAR = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": BTN_EDIT_YEAR
            },
            "color": "default"
        }],
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

KEYBOARD_END = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": BTN_END
            },
            "color": "default"
        }]
    ]
}

KEYBOARD_END_AND_CANCELE = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": BTN_END
            },
            "color": "default"
        }],
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
                "payload": "{\"button\": \"6\"}",
                "label": BTN_ADD_BROADCAST_BY_TIME
            },
            "color": "default"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"7\"}",
                    "label": BTN_BROADCAST_BY_TIME
                },
                "color": "default"
            }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": BTN_LEAVE_REASON
            },
            "color": "default"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"5\"}",
                    "label": BTN_ADRESSES
                },
                "color": "default"
            }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": BTN_ADMIN_EXIT
            },
            "color": "default"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"5\"}",
                    "label": BTN_LAST_MSG
                },
                "color": "default"
            }
        ]
    ]
}
