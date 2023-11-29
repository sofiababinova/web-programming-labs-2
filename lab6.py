from flask import Blueprint, request, render_template, redirect 
from Db import db
from Db.models import users, articles 
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint ("lab6", __name__)


@lab6. route("/lab6/check")
def main():
    my_users = users.query.all()
    print (my_users)

    my_articles = articles.query.all()
    print (my_articles)
    return "result in console!"

@lab6. route("/lab6/register", methods=["GET", "POST"])
def register ():
    errors = ''

    if request.method == "GET":
        return render_template("register.html", errors=errors)
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not (username_form or password_form):
        errors = "Пожалуйста, заполните все поля"
        return render_template('register.html', errors=errors)
    
    if len(password_form) < 5:
        errors = "Пароль должен содержать не менее 5 символов"
        return render_template('register.html', errors=errors)

    isUserExist = users.query.filter_by (username=username_form).first()
    
    if isUserExist is not None:
        errors = "Пользователь с данным именем уже существует"
        return render_template ("register.html", errors=errors)


    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db. session.commit()

    return redirect ("/lab6/login")