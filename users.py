'''
@author:
'''
import uuid

# this variable MUST be used as the name for the cookie used by this application
import bottle

import database

COOKIE_NAME = 'sessionid'


def check_login(db, usernick, password):
    """returns True if password matches stored"""
    cur = db.cursor()
    password = database.COMP249Db.encode(db, password)
    cur.execute("SELECT * FROM users WHERE password=? AND nick=?;", (password, usernick))
    result = cur.fetchall()
    db.conn.commit()
    if len(result) == 1:
        return True
    else:
        return False


# TODO sign cookies
def generate_session(db, usernick):
    """create a new session and add a cookie to the response object (bottle.response)
    user must be a valid user in the database, if not, return None
    There should only be one session per user at any time, if there
    is already a session active, use the existing sessionid in the cookie
    """
    cur = db.cursor()
    # TODO sanitize input
    cur.execute("SELECT * FROM sessions WHERE usernick=?;", (usernick,))
    db.conn.commit()
    result = cur.fetchone()
    if result is not None:
        sessionID = result[0]
        bottle.response.set_cookie(COOKIE_NAME, sessionID)
    else:
        sessionID = uuid.uuid4().hex
        cur.execute("INSERT INTO sessions VALUES (?,?)", (sessionID, usernick))
        db.conn.commit()
        bottle.response.set_cookie(COOKIE_NAME, sessionID)


# TODO sanitize inputs
def delete_session(db, usernick):
    """remove all session table entries for this user"""
    cur = db.cursor()
    cur.execute("DELETE FROM sessions WHERE usernick=(?);", (usernick,))
    db.conn.commit()


def session_user(db):
    """try to
    retrieve the user from the sessions table
    return usernick or None if no valid session is present"""
    cur = db.cursor()
    cookie = bottle.request.get_cookie('sessionid')
    if cookie is None:
        return None
    else:
        cur.execute("SELECT * FROM sessions WHERE sessionid=?;", (cookie,))
        result = cur.fetchone()
        db.conn.commit()
        if result is not None:
            return result[1]
        else:
            return None
