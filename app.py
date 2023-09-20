from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return '''
<!DOCTYPE html>
<html>
<link rel='stylesheet' href="''' + url_for('static', filename='lab1.css') + '''">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <div id="pusto"></div>
        
        <ol>
            <li>
                <a href="/lab1" target="_blank">Лабораторная работа 1</a>
            </li>
        </ol>
        <footer>
            &copy; Бабинова Софья, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
    return '''
<!DOCTYPE html>
<html>
<link rel='stylesheet' href="''' + url_for('static', filename='lab1.css') + '''">
    <head>
        <title>Бабинова Софья Евгеньевна, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        
        <div id="pusto"></div>

        <div>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div><br>

        <a href="http://127.0.0.1:5000/menu">Меню</a><br>

        <h2>Реализованные роуты</h2>

        <ul>
            <li>
                <a href="http://127.0.0.1:5000/lab1/oak">/lab1/oak - Дуб</a><br>
            </li> 

            <li>
                <a href="http://127.0.0.1:5000/lab1/student">/lab1/student - Студент</a><br>
            </li> 

            <li>
                <a href="http://127.0.0.1:5000/lab1/python">/lab1/python - Python</a><br>
            </li>

            <li>
                <a href="http://127.0.0.1:5000/lab1/nstu">/lab1/nstu - НГТУ</a><br>
            </li>
        </ul>
        <footer>
            &copy; Бабинова Софья, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
<link rel='stylesheet' href="''' + url_for('static', filename='lab1.css') + '''">
    <body id="dyb">
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''" id="oak">

    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
<link rel='stylesheet' href="''' + url_for('static', filename='lab1.css') + '''">
    <body id="student">
        <h1>Студент: Бабинова Софья Евгеньевна</h1>
        <img src="''' + url_for('static', filename='nstu.jpeg') + '''" id="nstu">

    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
<link rel='stylesheet' href="''' + url_for('static', filename='lab1.css') + '''">
    <body id="prog">
        <h1 id="zagolovok">Python</h1>
        <div>
        Python - высокоуровневый язык программирования общего назначения с динамической 
        строгой типизацией и автоматическим управлением памятью, ориентированный на 
        повышение производительности разработчика, читаемости кода и его качества, а также 
        на обеспечение переносимости написанных на нём программ. Язык является полностью 
        объектно-ориентированным в том плане, что всё является объектами. 
        </div><br>

        <div>
        Необычной особенностью языка является выделение блоков кода пробельными отступами. 
        Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает 
        необходимость обращаться к документации. Сам же язык известен как интерпретируемый 
        и используется в том числе для написания скриптов.
        </div><br>

        <div>
        Недостатками языка являются зачастую более низкая скорость работы и более высокое 
        потребление памяти написанных на нём программ по сравнению с аналогичным кодом, 
        написанным на компилируемых языках, таких как C или C++.
        </div><br>
        <img src="''' + url_for('static', filename='python.jpg') + '''" id="python">
    </body>
</html>
'''

@app.route("/lab1/nstu")
def nstu():
    return '''
<!DOCTYPE html>
<html>
<link rel='stylesheet' href="''' + url_for('static', filename='lab1.css') + '''">
    <body id="vyz">
        <h1 id="zagolovok">Новосибирский государственный технический университет</h1>
        <div>
         Университет был учрежден 19 августа 1950 г. как Новосибирский электротехнический институт. 
         В 1992 г. он был переименован в Новосибирский государственный технический университет (НГТУ). 
         С 2015 года полное название университета — Федеральное государственное бюджетное 
         образовательное учреждение высшего образования «Новосибирский государственный технический 
         университет» в связи с переименованием федерального государственного бюджетного 
         образовательного учреждения высшего профессионального образования «Новосибирский государственный 
         технический университет» в федеральное бюджетное образовательное учреждение высшего образования 
         «Новосибирский государственный технический университет» (приказ Министерства образования и 
         науки Российской Федерации № 128 от 26.02.2015 г.)
        </div><br>

        <div>
        В настоящий момент НГТУ является одним из крупнейших вузов региона: в университете обучается 
        более 13 200 студентов; работает более 1 500 преподавателей; осуществляется подготовка по 95 
        направлениям (бакалавриат и магистратура) и 5 специальностям высшего образования – 
        естественно-научным, техническим, экономическим и гуманитарным, а также по 7 специальностям 
        и направлениям среднего профессионального образования.
        </div><br>

        <div>
        В составе университета 16 факультетов и институтов: Факультет автоматики и вычислительной 
        техники (АВТФ), Факультет летательных аппаратов (ФЛА), Механико-технологический факультет 
        (МТФ), Факультет мехатроники и автоматизации (ФМА), Факультет пpикладной математики и информатики 
        (ФПМИ), Факультет радиотехники и электроники (РЭФ), Физико-технический факультет (ФТФ), Факультет 
        энергетики (ФЭН), Факультет бизнеса (ФБ), Факультет гуманитарного образования (ФГО), Институт 
        дистанционного обучения, единственный в регионе Институт социальных технологий и реабилитации, 
        Институт дополнительного профессионального образования, Факультет повышения квалификации, 
        Факультет довузовского образования, Народный факультет — для лиц пенсионного возраста, а 
        также Центр дистанционного довузовского образования.
        </div><br>
        <img src="''' + url_for('static', filename='vyz.jpg') + '''" id="ynik">
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Софья Бабинова'
    group = 'ФБИ-14'
    course = '3 курс'
    return render_template ('example.html', name=name, group=group, course=course)