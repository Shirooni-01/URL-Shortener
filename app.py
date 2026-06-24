from flask import Flask, render_template, request, redirect, url_for
import random
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uni_id TEXT UNIQUE,
            og_url TEXT
        )
    ''')

    conn.commit()
    conn.close()


init_db()


keys = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def uniqueid():
    uni_id = ''
    for i in range(6):
        uni_id += keys[random.randint(0, 35)]
    return uni_id


@app.route('/', methods=['GET', 'POST'])
def index():

    short_url = None

    if request.method == 'POST':

        og_url = request.form.get('long_url')

        if not og_url.startswith(('http://', 'https://')):
            og_url = 'https://' + og_url

        while True:

            uni_id = uniqueid()

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM urls WHERE uni_id=?",
                (uni_id,)
            )

            exist = cursor.fetchone()

            conn.close()

            if not exist:

                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()

                cursor.execute(
                    "INSERT INTO urls (uni_id, og_url) VALUES (?, ?)",
                    (uni_id, og_url)
                )

                conn.commit()
                conn.close()

                break

        short_url = url_for(
            'shorturl',
            uni_id=uni_id,
            _external=True
        )

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT uni_id, og_url FROM urls ORDER BY id DESC"
    )

    url_history = cursor.fetchall()

    conn.close()

    return render_template(
        'index.html',
        short_url=short_url,
        url_history=url_history
    )


@app.route('/<uni_id>')
def shorturl(uni_id):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT og_url FROM urls WHERE uni_id=?",
        (uni_id,)
    )

    url = cursor.fetchone()

    conn.close()

    if url:
        return redirect(url[0])

    return "URL Not Found"


if __name__ == "__main__":
    app.run(debug=True)