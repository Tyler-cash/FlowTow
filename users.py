'''
@author:
'''
import uuid

# this variable MUST be used as the name for the cookie used by this application
COOKIE_NAME = 'sessionid'


def check_login(db, usernick, password):
    """returns True if password matches stored"""


# TODO sign cookies
def generate_session(db, usernick):
    """create a new session and add a cookie to the response object (bottle.response)
    user must be a valid user in the database, if not, return None
    There should only be one session per user at any time, if there
    is already a session active, use the existing sessionid in the cookie
    """
    cur = db.cursor()
    # TODO sanitize input
    cur.execute("SELECT * FROM sessions WHERE usernick='" + usernick + "';")
    result = cur.fetchone()
    if result is not None:
        sessionID = result[0]
        bottle.response.set_cookie(COOKIE_NAME, sessionID)
    else:
        sessionID = uuid.uuid4().hex
        cur.execute("INSERT INTO sessions VALUES ('" + sessionID + "','" + usernick + "')")
        bottle.response.set_cookie('sessionid', sessionID)

# TODO sanitize inputs
def delete_session(db, usernick):
    """remove all session table entries for this user"""
    cur = db.cursor()
    cur.execute("DELETE FROM sessions WHERE usernick='" + usernick + "';")

def session_user(db):
    """try to
    retrieve the user from the sessions table
    return usernick or None if no valid session is present"""
