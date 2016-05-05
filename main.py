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

@application.route('/')
def home_page():
    return template('index', title="Home", usernick="None")


@application.post('/like')
def like_image():
    db = instanceOfDatabase.db
    liked_picture = request.forms.get('filename')
    if liked_picture is not None:
        interface.add_like(db, liked_picture)

    bottle.redirect('/', 303)


@application.route('/about')
def about_page():
    return template('about', title="About")


@application.route('/my')
def about_page():
    return template('my', title="My Profile")

    db = instanceOfDatabase.db
    if users.session_user(db):
        return template('my', title="My Profile")
    else:
        bottle.redirect('/', 303)


@application.route('/login')
def login_page():
    return template('login', title="Login")

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
