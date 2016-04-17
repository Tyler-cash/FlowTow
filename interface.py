'''
@author:
'''


def get_likes(cur):
    pass


def list_images(db, n, usernick=None):
    """Return a list of dictionaries for the first 'n' images in
    order of timestamp. Each dictionary will contain keys 'filename', 'timestamp', 'user' and 'comments'.
    The 'comments' value will be a list of comments associated with this image (as returned by list_comments).
    If usernick is given, then only images belonging to that user are returned."""
    cur = db.cursor()

    if usernick is None:
        cur.execute('SELECT * FROM images ORDER BY timestamp DESC;')  # LIMIT `' + str(n) + "`;")
    else:
        cur.execute('SELECT * FROM images WHERE `usernick`=`' + usernick + ' ORDER BY timestamp ASC;')  # LIMIT `' + str(n) + "`;")

    list_of_images = []

    for row in cur.fetchall():
        likes_cur = cur
        likes_cur.execute('SELECT `usernick` FROM likes WHERE `filename`=\'' + row[0] + "';")

        # TODO add list_comments to dictionary
        image = {'filename': row[0], 'timestamp': row[1], 'user': row[2], 'likes': len(likes_cur.fetchall())}
        list_of_images.append(image)

    return list_of_images


def add_image(db, filename, usernick):
    """Add this image to the database for the given user"""


def add_like(db, filename, usernick=None):
    """Increment the like count for this image"""


def count_likes(db, filename):
    """Count the number of likes for this filename"""
