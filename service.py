import model as m
import consts as c
import vklib as vk


def group_join(uid):
    uname = vk.get_user_name(uid)
    if uname == '':
        uname = 'No Name'
    m.add_bot_follower(uid, uname)


def message_processing(uid, text):
    if text.lover() in c.START_WORDS:
        uname = vk.get_user_name(uid)
        vk.send_message_keyboard(uid, c.WELCOME_TO_COURSE.format(uname), c.user_enroll_keyboard)


def group_leave(uid):
    uname = vk.get_user_name(uid)
    vk.send_message_keyboard(uid, c.GROUP_LEAVE_MESSAGE.format(uname), c.EMPTY_KEYBOARD)
