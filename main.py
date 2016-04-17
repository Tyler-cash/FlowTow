'''
@author:
'''
import bottle
from bottle import Bottle, template, debug, static_file, get, route
import interface
import users
from database import COMP249Db

COOKIE_NAME = 'sessionid'

app = Bottle()

@app.route('/')
def home_page():
    return template('index', title="Hello!", home="active", profile="", about="")


@app.route('/about')
def about_page():
    return template('about', title="About")


# Serves static files
@app.route('/static/images/<filename:path>')
def serve_images(filename):
    return bottle.static_file(filename, root='static/images')


@app.route('/static/js/<filename:path>')
def serve_javascripts(filename):
    return bottle.static_file(filename, root='static/js')


@app.route('/static/css/<filename:path>')
def serve_javascripts(filename):
    return bottle.static_file(filename, root='static/css')


if __name__ == '__main__':
    debug()
    app.run()
