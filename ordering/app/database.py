import sqlite3
from flask import g

DATABASE = 'app.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with get_db() as db:
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())

# Close connection after request ends
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
