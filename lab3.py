from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)

@lab3.route('/lab3/succes')
def succes():
    return render_template('succes.html')


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    surname = request.args.get('surname')
    if surname == '':
        errors['surname'] = 'Заполните поле!'

    name = request.args.get('name')
    if name == '':
        errors['name'] = 'Заполните поле!'

    middlename = request.args.get('middlename')
    if middlename == '':
        errors['middlename'] = 'Заполните поле!'

    age = request.args.get('age')
    if not age:
        errors['age'] = 'Заполните поле!'
    else:
        age = int(age)
        if age < 18 or age > 120:
            errors['age'] = 'Недопустимый возраст!'

    wherefrom = request.args.get('wherefrom')
    if wherefrom == '':
        errors['wherefrom'] = 'Заполните поле!'

    where = request.args.get('where')
    if where == '':
        errors['where'] = 'Заполните поле!'

    date = request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'

    tickettype = request.args.get('tickettype')
    shelf = request.args.get('shelf')
    luggage = request.args.get('luggage')
    return render_template('ticket.html', surname=surname, name=name, middlename=middlename, age=age, wherefrom=wherefrom, where=where, date=date, errors=errors, tickettype=tickettype, shelf=shelf, luggage=luggage)