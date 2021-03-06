#!/usr/bin/python
# -*- coding: utf-8 -*-

import consts as cnst

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

    def name_is_sign(self):
        return self.name is not None

    def email_is_sign(self):
        return self.email is not None

    def number_is_sign(self):
        return self.number is not None

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        if self.name_is_sign():
            self.email = email
        else:
            raise BaseException()

    def set_number(self, number):
        if self.name_is_sign() and self.email_is_sign():
            self.number = number
        else:
            raise BaseException()

    def reset(self):
        self.name = None
        self.email = None
        self.number = None

