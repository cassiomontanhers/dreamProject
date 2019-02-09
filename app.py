from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import jsonify
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
    # print(logged)
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

@app.route("/mydreams")
def mydreams():
    if check_session():
        dreams = get_all_dreams_from_user(session['uid'])
        return render_template('mydreams.html', dreams=dreams)
    else:
        setup()
        return render_template('login.html')
        session['uid'] = -1

@app.route("/logdream")
def logdream():
    if check_session():
        return render_template('logdream.html')
    else:
        setup()
        return render_template('login.html')
        session['uid'] = -1

@app.route('/adddream', methods=['POST'])
def adddream():
    info = str(request.form['info'])
    dream_date = str(request.form['date'])
    user_fk = session['uid']
    dream = (user_fk, dream_date, info)
    add_dream(dream)
    return mydreams()

@app.route('/get_rdn_dream', methods=['GET'])
def getRdnDream():
    dream = get_rdn_dream()
    feature_dream =	{
      "info": dream[3],
      "date": dream[2]
    }
    return jsonify(feature_dream)

def check_session():
    if session.get('uid'):
        if session.get('uid') >= 0:
            return True
    else:
        return False
        session['uid'] = -1
        session['username'] = null

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=4000)
