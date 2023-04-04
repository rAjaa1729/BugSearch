from flask import Flask,render_template,request, url_for, flash, redirect
from werkzeug.exceptions import abort
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sql@Prism1920",
        database="posts"
    )
    return connection

def get_post(post_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary= True)
    cursor.execute('SELECT * FROM post WHERE id = %s',(post_id,))
    post = cursor.fetchone()
    cursor.close()
    connection.close()
    if post is None:
        abort(404)
    return post


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM post')
    posts = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('INSERT INTO post (title, content) VALUES (%s,%s )',(title, content))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('index'))

    return render_template('create.html')

