#!/usr/bin/python
# -*- coding: utf-8 -*-

import consts as cnst
import datetime as dt

class Admin:
    def __init__(self, uid, name, status='member'):
        self.uid = uid
        self.name = name
        # self.status = status


class Follower:
    def __init__(self, uid, name, status='member', written_on_course=0, mess_allowed=0):
        self.uid = uid
        self.name = name
        self.status = status
        self.written_on_course = written_on_course
        self.mess_allowed = mess_allowed

    def is_msging_allowed(self):
        return self.mess_allowed == 1 and not self.status == cnst.USER_LEAVE_STATUS


class EnrollInfo:
    def __init__(self, uid):
        self.uid = uid
        self.name = None
        self.email = None
        self.number = None
        self.adress = None
        self.year = None

    def name_is_sign(self):
        return self.name is not None

    def email_is_sign(self):
        return self.email is not None

    def number_is_sign(self):
        return self.number is not None

    def adress_is_sign(self):
        return self.adress is not None

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        if self.name_is_sign():
            self.email = email
        else:
            raise BaseException()

    def set_number(self, number):
        self.number = number

    def set_adress(self, adress):
        if self.number_is_sign():
            self.adress = adress
        else:
            raise BaseException()

    def reset(self):
        self.name = None
        self.email = None
        self.number = None


# broadcast by time
class BcstByTime:
    def __init__(self, start_date=None, time=None, repet_days=None, msg=None, id=None):
        self.start_date = start_date
        self.time = time
        self.repet_days = repet_days
        self.msg = msg
        self.id = id

    def date_time_is_not_sign(self):
        return self.start_date is None or self.time is None or self.repet_days is None


class Adress:
    def __init__(self, name=None, lat=None, long=None, link="", id=0):
        self.name = name
        self.lat = lat
        self.long = long
        self.link = link
        self.id = id
        self.city = None
        self.street = None
        self.build_num = None

    def is_sign(self):
        return self.name is not None

    def get_links(self):
        if self.link is not None:
            return self.link.split(cnst.SEPARATOR)[:-1]
