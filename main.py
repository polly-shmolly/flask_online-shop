import sqlite3
from flask import Flask, render_template, request, \
    url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# db = SQLAlchemy(app)



# class Items(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     is_active = db.Column(db.Boolean, default=True)
#    # text = db.Column(db.Text)


def get_db_connection():
    conn = sqlite3.connect('shop_db.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(item_id):
    conn = get_db_connection()
    post = conn.execute("""SELECT * FROM items WHERE id = ?""",
                        (item_id, )).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('''SELECT * FROM items;''').fetchall()
    conn.close()
    return render_template('index.html', items=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']

    #     item = Items(title=title, price=price)
    #
    #     try:
    #         db.session.add(item)
    #         db.session.commit()
    #         return redirect('/')
    #     except:
    #         return 'You have error'
    # else:
    #     return render_template('create.html')

        if not title or not price:
            flash("Title and price are both required!")
        else:
            conn = get_db_connection()
            conn.execute("""INSERT INTO items (title, price) VALUES (?, ?)""",
                         (title, price))
            conn.commit()
            conn.close()
            return redirect('/')
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True) # false chtoby polzovatel ne videl oshibku


