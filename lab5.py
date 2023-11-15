from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, Blueprint, render_template, request, session
import psycopg2


lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_sofia",
        user="sofia_knowledge_base",
        password="111")
    
    return conn;


def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()
   
    print(result)


    dbClose(cur, conn)

    visibleuser = 'Anon'

    return render_template('lab5.html', username=visibleuser)


@lab5.route('/lab5/users')
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    
    result = cur.fetchall()

    users = []

    for i in range(len(result)):
        users.append(result[i][1])


    dbClose(cur, conn)

    return render_template('users.html', users=users)


@lab5.route('/lab5/register', methods=["GET", "POST"])
def register():
    errors = ''

    if request.method == "GET":
        return render_template('register.html', errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors = "Пожалуйста, заполните все поля"
        print(errors)
        return render_template('register.html', errors=errors)
    
    hashPassword = generate_password_hash(password)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s", (username))

    if cur.fetchone() is not None:
        errors = "Пользователь с данным именем уже существует"
        dbClose(cur, conn)
        return render_template('register.html', errors=errors)
    
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashPassword))

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login")


@lab5.route('/lab5/login', methods=["GET", "POST"])
def login():
    errors = ''

    if request.method == "GET":
        return render_template('login5.html', errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors = "Пожалуйста, заполните все поля"
        return render_template('login5.html', errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s", (username))

    result = cur.fetchone()

    if result is None:
        errors = "Неправильный логин или пароль"
        dbClose(cur, conn)
        return render_template('login5.html', errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return render_template('lab5.html', username=username)
    else:
        errors = "Неправильный логин или пароль"
        return render_template('login5.html', errors=errors)
    

@lab5.route('/lab5/new_article', methods=["GET", "POST"])
def createarticle():
    errors = ''

    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html")
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors = "Заполните текст"
                return render_template("new_article.html", errors=errors)
            
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id", (userID, title, text_article))

            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")
        
        return redirect("/lab5/login")
    

@lab5.route('/lab5/articles/<int:article_id>')
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody=cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        
        text = articleBody[1].splitlines()

        return render_template("article.html", article_text=text, article_title=articleBody[0], username=session.get("username"))