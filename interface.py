'''
@author:
'''
import datetime


def list_images(db, n, usernick=None):
    """Return a list of dictionaries for the first 'n' images in
    order of timestamp. Each dictionary will contain keys 'filename', 'timestamp', 'user' and 'comments'.
    The 'comments' value will be a list of comments associated with this image (as returned by list_comments).
    If usernick is given, then only images belonging to that user are returned."""
    cur = db.cursor()

    if usernick is None:
        cur.execute('SELECT * FROM images ORDER BY timestamp DESC;')
    else:
        cur.execute('SELECT * FROM images WHERE `usernick`=`' + usernick + '` ORDER BY timestamp DESC;')

    list_of_images = []
    i = 0;

    for row in cur.fetchall():
        if i > n - 1:
            break
        else:
            i += 1

        image = {'filename': row[0], 'timestamp': row[1], 'user': row[2], 'likes': count_likes(db, row[0])}
        list_of_images.append(image)

    return list_of_images


def add_image(db, filename, usernick):
    """Add this image to the database for the given user"""
    cur = db.cursor()
    cur.execute("INSERT INTO images VALUES('" + filename + "','" + str(datetime.datetime.now()) + "', '" + usernick + "');")



def add_like(db, filename, usernick=None):
    """Increment the like count for this image"""
    cur = db.cursor()

    if usernick is None:
        # Ensures file exists
        cur.execute("SELECT * FROM images WHERE filename='" + filename + "';")
        if len(cur.fetchall()) < 1:
            return

        cur.execute("INSERT INTO likes VALUES('" + filename + "', NULL)")
        db.conn.commit()
    else:
        # Ensures user exists
        cur.execute("SELECT * FROM users WHERE `nick`='" + usernick + "'")
        if len(cur.fetchall()) < 1:
            return
        # Ensures file exists
        cur.execute("SELECT * FROM images WHERE `filename`='" + filename + "'")
        if len(cur.fetchall()) < 1:
            return

            # TODO possibly add check to see if user has liked picture
        cur.execute("INSERT INTO likes VALUES('" + filename + "', '" + usernick + "');")
        db.conn.commit()


def count_likes(db, filename):
    """Count the number of likes for this filename"""
    cur = db.cursor()
    cur.execute("SELECT `usernick` FROM likes WHERE `filename`='" + filename + "';")
    return len(cur.fetchall())