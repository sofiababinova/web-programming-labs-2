from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route('/lab2/example')
def example():
    name, group, course, lab_num = 'Софья Бабинова', 'ФБИ-14', '3 курс', 'Лабораторная 2'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]

    books = [
        {'book': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'genre': 'Роман', 'pages': 528},
        {'book': 'По ком звонит колокол', 'author': 'Эрнест Хэмингуэй', 'genre': 'Роман', 'pages': 704},
        {'book': 1984, 'author': 'Джордж Оруэлл', 'genre': 'Роман', 'pages': 320},
        {'book': 'Над пропастью во ржи', 'author': 'Джером Дэвид Сэлинджер', 'genre': 'Роман', 'pages': 234},
        {'book': 'Маленький принц', 'author': 'Антуан де Сент-Экзюпери', 'genre': 'Сказка', 'pages': 128},
        {'book': 'Гамлет', 'author': 'Уильям Шекспир', 'genre': 'Трагедия', 'pages': 384},
        {'book': 'Три товарища', 'author': 'Эрих Мария Ремарк', 'genre': 'Роман', 'pages': 480},
        {'book': 'Великий Гэтсби', 'author': 'Фрэнсис Скотт Фицджеральд', 'genre': 'Роман', 'pages': 256},
        {'book': '451° по Фаренгейту', 'author': 'Рэй Бредбери', 'genre': 'Роман', 'pages': 256},
        {'book': 'Убить пересмешника', 'author': 'Харпер Ли', 'genre': 'Роман', 'pages': 416}
    ]
    return render_template ('example.html', name=name, group=group, course=course, lab_num=lab_num, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/like')
def like():
    return render_template('like.html')