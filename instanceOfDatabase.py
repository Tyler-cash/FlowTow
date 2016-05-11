from database import COMP249Db

# TODO instantiate db??
global db
db = COMP249Db()


def reset_database():
    db = COMP249Db.create_tables()
    db = COMP249Db.sample_data()
