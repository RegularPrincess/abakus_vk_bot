#!/usr/bin/python
# -*- coding: utf-8 -*-

class Admin:
    def __init__(self, uid, name, status='member'):
        self.uid = uid
        self.name = name
        # self.status = status


class Follower:
    def __init__(self, uid, name, status='member'):
        self.uid = uid
        self.name = name
        self.status = status


class Enroll_info:
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

