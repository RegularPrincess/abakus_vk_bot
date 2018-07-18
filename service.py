import model as m


def group_join(uid, uname):
    if uname == '':
        uname = 'No Name'
    m.add_bot_follower(uid, uname)