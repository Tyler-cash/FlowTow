'''
@author:
'''
import bottle
from bottle import Bottle, request, template, debug

import instanceOfDatabase
import interface

COOKIE_NAME = 'sessionid'

application = Bottle()

@application.route('/')
def home_page():
    return template('index', title="Home")


@application.post('/like')
def like_image():
    liked_picture = request.forms.get('filename')
    if liked_picture is not None:
        interface.add_like(db, liked_picture)

    bottle.redirect('/', 303)


@application.route('/about')
def about_page():
    return template('about', title="About")


@application.route('/profile')
def about_page():
    return template('profile', title="Profile")


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
    db = instanceOfDatabase.db

    debug()
    application.run()
