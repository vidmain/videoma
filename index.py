# coding: utf-8
import os
os.chdir(os.path.dirname(__file__))

from bottle import get, default_app, debug, template, request
import psycopg2

try:
    conn = psycopg2.connect("dbname='video' user='puser' host='localhost' password='b2XtUat5QH'")
    conn.set_isolation_level(0)
except:
    pass


def db_exec(cur, sql_exec):
    try:
        result = cur.execute(sql_exec)
        return result
    except:
        result = -1


@get('/')
def main():
    output = template('make_table', rows=['dsadsa', 'fsdfsdafsdf', '4', '10'])
    return output

# Регистрация
@get('/register', method='GET')
def main():
    if request.GET.get('save','').strip():
        cur = conn.cursor()
        email = request.GET.get('email', '').strip()
        login = request.GET.get('login', '').strip()
        password = request.GET.get('password', '').strip()
        repassword = request.GET.get('repassword', '').strip()
        if password != repassword:
            return template('templates/register_main.tpl')
        query = """INSERT INTO users (login, password, email, reg_data) VALUES ('%s', '%s', '%s', '1993-12-12')""" % (login, password, email);
        res = cur.execute(query)
        conn.close()
    else:
        return template('templates/register_main.tpl')



@get('/postgres')
def main():
    try:
        conn = psycopg2.connect("dbname='vidmain' user='postuser' host='localhost' password='192837'")
        return "5 минут, полет нормальный!"
    except:
        return "I am unable to connect to the database"
    
@get('/video/<video_id>')
def main(video_id):
    return template('templates/video_main.tpl', video_id=video_id)

"""@get('/:name')
def main(name):
    return 'Page: ' + name
"""

debug(True)
application = default_app()
