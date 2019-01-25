from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
app.secret_key = "super secret key"

def setup():
    test_connection()
    # drop_table('users');
    create_table_users()
    create_table_dreams()

from connection import *

@app.route('/')
def home():
    if check_session():
        return render_template('main.html')
    else:
        setup()
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    logged = verify_login(POST_USERNAME, POST_PASSWORD)
    print(logged)
    if logged:
        session['username'] = logged[1]
        session['uid'] = logged[0]
        return render_template('main.html')
    return home()

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def do_signup():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_EMAIL = str(request.form['email'])
    user = (POST_USERNAME, POST_PASSWORD, POST_EMAIL)
    add_user(user)
    return home()

@app.route("/logout")
def logout():
    session['uid'] = -1
    return home()

def check_session():
    if session.get('uid'):
        if session.get('uid') >= 0:
            return True
    else:
        return False
        session['uid'] = -1
        session['username'] = null

if __name__ == "__main__":
    app.run(debug=True, port=4000)
