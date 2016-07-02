'''
@author:
'''
import os

import bottle
from bottle import Bottle, request, template, debug

import comments
import instanceOfDatabase
import interface
import users

COOKIE_NAME = 'sessionid'

application = Bottle()


def hide_my_images():
    """
    Returns hidden if user is not logged in and if user is logged in returns ""
    """
    db = instanceOfDatabase.db
    users_status = ""
    # If user is not logged in hide my images
    if users.session_user(db) is None:
        users_status = "hidden"

    return users_status


@application.route('/')
def home_page():
    """
    Returns the homepage
    """
    return template('index', title="Home", usernick="None", loggedIn=hide_my_images())


@application.route('/about')
def about_page():
    """
    Returns the about flowtow page
    """
    return template('about', title="About", loggedIn=hide_my_images())


@application.route('/my')
def my_profile_page():
    """
    If the user isn't logged in they will be redirected to
    the homepage else this will return a page of all the user's
    uploaded images.
    """
    db = instanceOfDatabase.db
    if users.session_user(db) is not None:
        return template('my', title="My Profile", loggedIn=hide_my_images())
    else:
        return bottle.redirect('/', 303)


@application.route('/login')
def login_page():
    """
    Returns the login page
    """
    return template('login', title="Login", errors="hidden", loggedIn=hide_my_images())


@application.route('/login-failed')
def login_failed():
    """
    Returns the login page. This is shown when a user's
    submitted credentials can't be found in the db.
    """
    return template('login', title="Login", errors="", loggedIn=hide_my_images())


@application.route('/comments/<filename>')
def comments_page(filename):
    """
    Returns a page with the discussions of a particular image
    """
    if "jpg" in filename:
        db = instanceOfDatabase.db
        image = interface.get_image(db, filename)
        bottle.response.set_cookie('filename', filename)
        filename = filename.replace(".jpg", "")
        # Redirects to url without filetype in url so that it's prettier
        return bottle.redirect('/comments/' + filename)
    else:
        # If filename cookie not set then the user is reloading the page and
        # therefore the comments page won't load.
        test = bottle.request.get_cookie('filename')
        if test is None:
            return bottle.redirect('/comments/' + filename + ".jpg")

        return template('comment', title="Comments", loggedIn=hide_my_images())


# Post method handlers
@application.post('/logout')
def logout_user():
    """
    This method logs a user out of the site.
    """
    db = instanceOfDatabase.db
    user_nick = users.session_user(db)
    users.delete_session(db, user_nick)
    return bottle.redirect('/', 303)


@application.post('/like')
def like_image():
    """
    This method deals with the logic related to liking
    an image.
    """
    db = instanceOfDatabase.db
    liked_picture = request.forms.get('filename')
    if liked_picture is not None:
        interface.add_like(db, liked_picture)

    return bottle.redirect('/', 303)


@application.post('/login')
def login_user():
    """
    This method deals with logging a user in or alerting
    the user their credentials can't be found in the db.
    """
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
    """
    This method uploads files to the server.
    """
    db = instanceOfDatabase.db
    user = users.session_user(db)
    if user is None:
        return bottle.redirect('/', 303)
    image_file = request.files.get('imagefile')
    if image_file is None:
        return 'No image submitted'
    if image_file.content_type != 'image/jpg':
        return "Only jpg files allowed"

    if os.name == 'posix':
        save_path = os.path.join(os.getcwd() + '/static/images/')
    else:
        save_path = os.path.join(os.getcwd() + '\\static\\images\\')
    image_file.save(save_path)
    interface.add_image(db, image_file.filename, user)

    return bottle.redirect('/my', 303)


@application.post('/submit-comment')
def comment_on_image():
    db = instanceOfDatabase.db
    usernick = users.session_user(db)
    if usernick is not None:
        comment = bottle.request.forms.get("comment")
        filename = bottle.request.forms.get("filename")
        comments.add_comment(db, comment, usernick, filename)
        return bottle.redirect('/', 302)
    else:
        return "Sorry, you must be logged in to comment."


# Serves static files
@application.route('/static/images/<filename:path>')
def serve_images(filename):
    """
    This method serves all the relevant images.
    """
    return bottle.static_file(filename, root='static/images')


@application.route('/static/js/<filename:path>')
def serve_javascripts(filename):
    """
    This method serves all the relevant javascript.
    """
    return bottle.static_file(filename, root='static/js')


@application.route('/static/css/<filename:path>')
def serve_css_sheets(filename):
    """
    This method serves all the relevant style sheets.
    """
    return bottle.static_file(filename, root='static/css')


if __name__ == '__main__':
    application.run()
