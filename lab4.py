from xml.dom.expatbuilder import DOCUMENT_NODE
from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    errors = {}
    
    if request.method == 'GET':
        return render_template('login.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == '':
        errors['username'] = 'Не введен логин!'

    if password == '':
        errors['password'] = 'Не введен пароль!'

    if username == 'alex' and password == '123':
        return render_template('success.html', username=username, password=password)
    elif username != '' and password != '':
        error = 'Неверные логин и/или пароль'
        return render_template('login.html', error=error, errors=errors, username=username, password=password)
    return render_template('login.html', errors=errors, username=username, password=password)

    
@lab4.route('/lab4/success')
def success():
    return render_template('success.html')