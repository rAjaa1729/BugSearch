import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "142857",
        database = "BugSearch"
    )
    return mydb

def get_user(user_id,email_id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    if user_id:
        cur.execute('SELECT * FROM Users WHERE user_id = %s',(user_id,))
    if email_id:
        cur.execute('SELECT * FROM Users WHERE email_id = %s',(email_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user 

app = Flask(__name__)
app.config['SECRET_KEY'] = '142857'

@app.route('/')
def login_home():
    return render_template('login_home.html')

@app.route('/<int:user_id>/user_home')
def user_home(user_id):
    user = get_user(user_id, None)
    return render_template('user_home.html')

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        email_id = request.form['email_id']
        user = get_user(None,email_id)
        username = request.form['username']
        passcode = request.form['passcode']
        if not email_id:
            flash('Email address is required!')
        elif not username:
            flash('Username is required!')
        elif not passcode:
            flash('Please set password!')
        elif user is not None :
            flash('This email address is already registered!')
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT username FROM Users WHERE username=%s",(username,))
            if cur.fetchone() is not None:
                flash("Username already exist please enter new username")
                conn.commit()
                conn.close()
                return render_template('signup.html',username=username,email_id=email_id,password=passcode)
            cur.execute("SELECT username FROM Users WHERE username=%s AND email_id=%s",(username,email_id))
            if cur.fetchone() is not None:  
                flash("Account with this username and password already exist please login")
                conn.commit()
                conn.close()
                return render_template('signup.html',username=username,email_id=email_id,password=passcode)
            cur.execute('INSERT INTO Users (email_id, username, passcode) VALUES (%s, %s, %s)',(email_id, username, passcode))
            cur.execute('SELECT LAST_INSERT_ID()')
            flash("Account created successfully")
            user_id = cur.fetchone()[0]
            conn.commit()
            conn.close()
            return redirect(url_for('user_home', user_id=user_id))
    return render_template('signup.html')
        

@app.route("/users/login",methods=["GET","POST"])
def userlogin():
    if (request.method=="POST"):
        username=request.form["username"]
        password=request.form["password"]
        if not username:
            flash("Username is required")
        elif not password:
            flash("Password is required")
        else:
            conn = get_db_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT user_id FROM Users WHERE username=%s AND passcode=%s", (username, password))
            user = cur.fetchone()
            conn.close()
            cur.close()
            if user is None:
                flash("Incorrect password or username")
                return render_template('login.html')
            user_id = user[0]
            return redirect(url_for('user_home', user_id=user_id))

            

                






