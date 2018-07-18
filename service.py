import model as m
import consts as c
import vklib as vk


def group_join(uid, uname):
    if uname == '':
        uname = 'No Name'
    m.add_bot_follower(uid, uname)


def message_processing(uid, text):
    if text.lover() in c.START_WORDS:
        pass


def group_leave(uid):
    uname = vk.get_user_name(uid)
    vk.send_message(uid, c.group_leave_text.format(uname))
