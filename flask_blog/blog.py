import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort 

def get_db_connection():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "142857",
        database = "db"
    )
    # conn.row_factory = sqlite3.Row
    return mydb

def get_post(post_id):
    con = get_db_connection()
    conn = con.cursor()
    conn.execute('SELECT * FROM posts WHERE id = %s',
                        (post_id,))
    post = conn.fetchone()
    con.close()
    if post is None:
        abort(404)
    return post 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    con = get_db_connection()
    conn = con.cursor()
    conn.execute('SELECT * FROM posts')
    posts = conn.fetchall()
    con.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            con = get_db_connection()
            conn = con.cursor()
            conn.execute('INSERT INTO posts (title, content) VALUES (%s, %s)',
                            (title, content))
            con.commit()
            con.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            con = get_db_connection()
            conn = con.cursor()
            conn.execute('UPDATE posts SET title = %s, content = %s'
                        'WHERE id = %s',
                        (title, content, id))
            con.commit()
            con.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    con = get_db_connection()
    conn = con.cursor()
    conn.execute('DELETE FROM posts WHERE id = %s', (id,))
    con.commit()
    con.close()
    flash('"{}" was successfully deleted!'.format(post[2]))
    return redirect(url_for('index'))