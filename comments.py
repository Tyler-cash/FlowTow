import time


def add_comment(db, comment, usernick, filename):
    cur = db.cursor()
    date = str(time.strftime("%Y-%m-%d %H:%M:%S"))
    cur.execute("INSERT INTO comments VALUES (?,?,?,?)", (filename, usernick, date, comment))
    db.conn.commit()


def list_comments(db, filename, n):
    """
    Returns n amount of comments from filename image.
    @:rtype list
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM comments WHERE filename=? ORDER BY timestamp DESC;", (filename,))
    results = cur.fetchall()
    i = 0
    outputted_rows = []
    for row in results:
        i += 1
        if i > n:
            break

        outputted_rows.append(row)
    return outputted_rows
