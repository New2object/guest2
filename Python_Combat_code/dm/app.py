import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)  # create the application instance :)
# app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'defect.db'),
    SECRET_KEY='development key'
))
app.config.from_envvar('DM_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def all_defects():
    db = get_db()
    cur = db.execute(
        'SELECT defects.*, tags.title AS tag_name,tags.type AS tag_type FROM defects JOIN tags ON defects.tag_id = tags.id ORDER BY id DESC')
    defects = cur.fetchall()
    return render_template('index.html', defects=defects)


@app.route("/new")
def new():
    db = get_db()
    cur = db.execute('SELECT id,title FROM tags ORDER BY id DESC')
    tags = cur.fetchall()
    return render_template('new.html', tags=tags)


@app.route("/create_defect", methods=['POST'])
def create():
    db = get_db()
    # ? 表示占位符,防止sql注入
    cur = db.execute('INSERT INTO defects VALUES (NULL ,?,?,?,?)',
                     [request.form['title'], request.form['content'],
                      request.form['author'], request.form['tag_id']])
    db.commit()
    # 重定向
    flash('创建成功')
    return redirect(url_for('all_defects'))


# /edit/12 ok
# /edit/abc error
@app.route("/edit/<int:defect_id>")  # 这是一个get
def edit(defect_id):
    db = get_db()

    cur = db.execute('SELECT * FROM defects WHERE id=?', [defect_id])
    defect = cur.fetchone()
    if defect is None:
        return redirect(url_for('all_defects'))
    cur = db.execute('SELECT id,title FROM tags ORDER BY id DESC ')
    tags = cur.fetchall()
    return render_template('edit.html', defect=defect, tags=tags)


@app.route("/update_defect/<int:defect_id>", methods=['POST'])
def update(defect_id):
    db = get_db()
    # ? 表示占位符,防止sql注入
    cur = db.execute('UPDATE defects SET title=?,content=?,author=?,tag_id=? WHERE id= ? ',
                     [request.form['title'], request.form['content'],
                      request.form['author'], request.form['tag_id'], defect_id])
    db.commit()
    # 重定向
    flash('编辑成功')
    return redirect(url_for('all_defects'))


@app.route("/delete/<int:defect_id>")  # 这是一个get
def delete(defect_id):
    db = get_db()

    cur = db.execute('SELECT * FROM defects WHERE id=?', [defect_id])
    defect = cur.fetchone()
    if defect is None:
        return redirect(url_for('all_defects'))
    cur = db.execute('DELETE  FROM defects  WHERE id= ? ', [defect_id])
    db.commit()
    flash('删除成功')
    return redirect(url_for('all_defects'))


@app.route("/show/<int:defect_id>")  # 这是一个get
def show(defect_id):
    db = get_db()

    cur = db.execute(
        'SELECT defects.*, tags.title AS tag_name,tags.type AS tag_type FROM defects JOIN tags ON defects.tag_id = tags.id WHERE defects.id=?',
        [defect_id])

    defect = cur.fetchone()
    if defect is None:
        flash('该缺陷不存在')
        return redirect(url_for('all_defects'))
    return render_template('show.html', defect=defect)
