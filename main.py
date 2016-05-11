'''
@author:
'''
import os

import bottle
from bottle import Bottle, request, template, debug

import instanceOfDatabase
import interface
import users

COOKIE_NAME = 'sessionid'

application = Bottle()


# Returns hidden if user is not logged in and if user is logged in returns ""
def hidden_my_images():
    db = instanceOfDatabase.db
    users_status = ""
    # If user is not logged in hide my images
    if users.session_user(db) is None:
        users_status = "hidden"

    return users_status


@application.route('/')
def home_page():
    return template('index', title="Home", usernick="None", loggedIn=hidden_my_images())


@application.route('/about')
def about_page():
    return template('about', title="About", loggedIn=hidden_my_images())


@application.route('/my')
def about_page():
    db = instanceOfDatabase.db
    if users.session_user(db) is not None:
        return template('my', title="My Profile", loggedIn=hidden_my_images())
    else:
        return bottle.redirect('/', 303)


@application.route('/login')
def login_page():
    return template('login', title="Login", errors="hidden", loggedIn=hidden_my_images())


@application.route('/login-failed')
def login_failed():
    return template('login', title="Login", errors="", loggedIn=hidden_my_images())


@application.route('/logout')
def logout_user():
    db = instanceOfDatabase.db
    user_nick = users.session_user(db)
    users.delete_session(db, user_nick)
    return bottle.redirect('/', 303)


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
        return bottle.redirect('/', 303)
    else:
        return login_failed()


@application.post('/upload')
def upload_file():
    db = instanceOfDatabase.db
    user = users.session_user(db)
    if user is None:
        return bottle.redirect('/', 303)
    image_file = request.files.get('imagefile')
    if image_file is None:
        return 'No image submitted'
    if image_file.content_type != 'image/jpg' and image_file.content_type != 'image/jpeg':
        return "Only jpg files allowed"

    save_path = os.path.join(os.getcwd() + '\\static\\images\\', )
    image_file.save(save_path)
    interface.add_image(db, image_file.filename, user)

    return bottle.redirect('/my', 303)


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
