from flask import Blueprint, render_template
lab6 = Blueprint('lab6', __name__)


@lab6.route('/lab4/')
def lab():
    return render_template('lab6.html')