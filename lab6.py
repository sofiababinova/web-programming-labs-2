from flask import Blueprint, request, render_template, redirect 
from Db import db
from Db.models import users, articles 
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint ("lab6", __name__)


@lab6.route('/lab6/')
def lab():
    visibleuser = 'Anon'
    return render_template('lab6.html', username_form=visibleuser)


@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print (my_users)

    my_articles = articles.query.all()
    print (my_articles)
    return "result in console!"

@lab6.route("/lab6/register", methods=["GET", "POST"])
def register ():
    errors = ''

    if request.method == "GET":
        return render_template("register6.html", errors=errors)
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not (username_form or password_form):
        errors = "Пожалуйста, заполните все поля"
        return render_template('register6.html', errors=errors)
    
    if len(password_form) < 5:
        errors = "Пароль должен содержать не менее 5 символов"
        return render_template('register6.html', errors=errors)

    isUserExist = users.query.filter_by (username=username_form).first()
    
    if isUserExist is not None:
        errors = "Пользователь с данным именем уже существует"
        return render_template ("register6.html", errors=errors)


    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db. session.commit()

    return redirect ("/lab6/login")


@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    errors = ''

    if request.method == "GET":
        return render_template ("login6.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not (username_form or password_form):
        errors = "Пожалуйста, заполните все поля"
        return render_template('login6.html', errors=errors)

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is None:
        errors = "Пользователь не существует"
        return render_template('login6.html', errors=errors)

    if not check_password_hash(my_user.password, password_form):
        errors = "Неправильный пароль"
        return render_template('login6.html', errors=errors)

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return render_template ("lab6.html", username_form=username_form)
    return render_template ("login6.html")


@lab6.route('/lab6/new_article', methods=["GET", "POST"])
@login_required
def createarticle():
    errors = ''

    if request.method == "GET":
        return render_template("new_article6.html", errors=errors)
        
    if request.method == "POST":
        text_article = request.form.get("text_article")
        title = request.form.get("title_article")
        is_public = request.form.get("is_public") == "on"

        if len(text_article) == 0:
            errors = "Заполните текст"
            return render_template("new_article6.html", errors=errors)
    
        if len(title) == 0:
            errors = "Введите название"
            return render_template("new_article6.html", errors=errors)
            
        new_article = articles(title=title, article_text=text_article, is_public=is_public, user_id=current_user.id)
        db.session.add(new_article)
        db.session.commit()

        return redirect(f"/lab6/articles/{new_article.id}")
        
    return redirect("/lab6/login")
    

@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def getArticle(article_id):
    article = articles.query.get(article_id)

    if article is None:
        return "Заметка не найдена"

    paragraphs = article.article_text.split('\n')

    return render_template("article6.html", article=article, paragraphs=paragraphs)


@lab6.route('/lab6/view_article/')
@login_required
def viewArticle():

    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    username = current_user.username
    
    return render_template('view_article6.html', articles=my_articles, username=username)


@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6/")