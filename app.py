from database import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session
import random
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def home():
    if 'name' in login_session and login_session['name'] != None:
        return logged_in()
    print(request.remote_addr)
    print(type(request.remote_addr))
    print("HERE")
    if int(request.remote_addr[-1])%2==0:
        version = "A"
    else:
        version = "B"
    create_metric("visit home",version,datetime.datetime.now(),"Anon")
    return render_template('home'+version+'.html')
    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        return logged_in()
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    if int(request.remote_addr[-1])%2==0:
        version = "A"
    else:
        version = "B"
    create_metric("clicked sign up",version,datetime.datetime.now(),"")
    #check that username isn't taken
    user = get_user(request.form['username'])
    if user == None:
        create_metric("user "+request.form['username']+" made",version,datetime.datetime.now(),request.form['username'])
        create_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logged-in')
def logged_in():
    return render_template('logged.html')


@app.route('/logout')
def logout():
    login_session['name'] = None
    return home()



if __name__ == '__main__':
    app.run(host='0.0.0.0')
