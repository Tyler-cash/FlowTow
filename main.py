'''
@author:
'''
import bottle
from bottle import Bottle, request, template, debug

import instanceOfDatabase
import interface
import users

COOKIE_NAME = 'sessionid'

application = Bottle()


# Redirects
@application.route('/')
def home_page():
    return template('index', title="Home", usernick="None")


@application.route('/about')
def about_page():
    return template('about', title="About")


@application.route('/my')
def about_page():
    db = instanceOfDatabase.db
    if users.session_user(db) is not None:
        return template('my', title="My Profile")
    else:
        return bottle.redirect('/', 303)

@application.route('/login')
def login_page():
    return template('login', title="Login", errors="hidden")


@application.route('/login-failed')
def login_failed():
    return template('login', title="Login", errors="")


# Post method handlers
@application.post('/like')
def like_image():
    db = instanceOfDatabase.db
    liked_picture = request.forms.get('filename')
    if liked_picture is not None:
        interface.add_like(db, liked_picture)

    return bottle.redirect('/', 303)


@application.post('/login')
def login_user():
    db = instanceOfDatabase.db
    username = request.forms.get('nick')
    password = request.forms.get('password')

    if username is "" or password is "":
        return login_failed()

    if users.check_login(db, username, password):
        users.generate_session(db, username)
        return bottle.redirect('/my', 303)
    else:
        return login_failed()


# Serves static files
@application.route('/static/images/<filename:path>')
def serve_images(filename):
    return bottle.static_file(filename, root='static/images')


@application.route('/static/js/<filename:path>')
def serve_javascripts(filename):
    return bottle.static_file(filename, root='static/js')


@application.route('/static/css/<filename:path>')
def serve_javascripts(filename):
    return bottle.static_file(filename, root='static/css')


if __name__ == '__main__':
    debug()
    application.run()
