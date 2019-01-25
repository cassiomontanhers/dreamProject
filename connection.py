import sqlite3
import sys


def create_connection():
    try:
        conn = sqlite3.connect("dreambs/dream.db")
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def drop_table(table_name):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("DROP TABLE users")
        data = cur.fetchone()
        print ("DROPPED table " + table_name)
    except sqlite3.Error as e:
        print ("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if conn:
            conn.close()

def test_connection():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print ("SQLite version: %s" % data)
    except sqlite3.Error as e:
        print ("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if conn:
            conn.close()


def create_table_users():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        _id INTEGER PRIMARY KEY,
        name text NOT NULL,
        password text NOT NULL,
        email text NOT NULL
        );""")
        data = cur.fetchone()
        print ("Created table users")
    except sqlite3.Error as e:
        print ("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if conn:
            conn.close()


def create_table_dreams():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS dreams (
        id integer PRIMARY KEY,
        info text NOT NULL
        );""")
        data = cur.fetchone()
        print ("Created table dreams")
    except sqlite3.Error as e:
        print ("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if conn:
            conn.close()

# =======================================================================INSERTS

def add_user(user):
    conn = create_connection()
    sql = ''' INSERT INTO users VALUES(null,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    conn.close()
    return cur.lastrowid

def get_all_user():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def verify_login(username, password):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name=? AND password=?", (username, password))
    rows = cur.fetchone()

    if rows:
        print(rows)
    else:
        print("Empty Return")
        
    return rows
