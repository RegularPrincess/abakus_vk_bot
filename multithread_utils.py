from threading import Thread

import time

import db_utils as db


class Thread_allow_updater(Thread):
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)

    def run(self):
        """Запуск потока, который обновляет инфу о возможности писать пользователям каждые 4 часа"""
        while True:
            print('thread start')
            db.update_mess_allowed_info()
            time.sleep(14400)
