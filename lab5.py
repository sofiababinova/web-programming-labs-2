from flask import redirect, Blueprint, render_template, request
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

    return 'go to console'


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