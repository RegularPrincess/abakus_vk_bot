## -*- coding: utf-8 -*-
#Кнопки

GOODS = "🎁 Товары и услуги"
BASKET = "🛒 Корзина"
CHECKOUT = "📝 Оформить заказ"
CANCEL = "⛔ Отмена"

BROADCAST = "Рассылка"
ADD_GOODS = "Добавить товар/услугу"
ADD_CAT = "Добавить категорию"
EDIT_CAT = "Изменить категорию"
EDIT_GOODS = "Изменить товар/услугу"
ADD_ADMIN = "Добавить администратора"
ADMINS = "Администраторы"
SUBS = "Подписчики"
MENU = "Меню пользователя"


group_join_text = '''
Приветствуем, {!s}! 
'''

user_menu_keyboard = {
                "one_time": False,
                "buttons": [
                    [{
                        "action": {
                        "type": "text",
                            "payload": "{\"button\": \"1\"}",
                            "label": GOODS
                        },
                        "color": "default"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"2\"}",
                            "label": BASKET
                        },
                        "color": "default"
                    }],
                    [{
                        "action": {
                            "type": "text",
                            "payload": "{\"button\": \"3\"}",
                            "label": CHECKOUT
                        },
                        "color": "default"
                    }]
                ]
            }


user_cancel_keyboard = {
                "one_time": False,
                "buttons": [
                    [{
                        "action": {
                        "type": "text",
                            "payload": "{\"button\": \"1\"}",
                            "label": GOODS
                        },
                        "color": "default"
                    }]
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
                        "color": "negative"
                    }]
                ]
            }


group_leave_text = '''
Ждем тебя снова!
'''

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

