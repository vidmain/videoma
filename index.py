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
    return template('templates/register_main.tpl')
    
@get('/register/send', method='POST')
def main():
    if request.POST.get('login','').strip():
        # Для работы с бд
        cur = conn.cursor()

        # Получаем данные
        email = request.GET.get('email', '').strip()
        login = request.GET.get('login', '').strip()
        password = request.GET.get('password', '').strip()
        password2 = request.GET.get('password2', '').strip()
        name = request.GET.get('name', '').strip()
        birthday = request.GET.get('birthday', '').strip()

        # Проверяем корректность введенных данных
        if password != password2:
            return 'ОШИБОЧКА'
        
        if len(email) > 64 and len(email) < 6:
            return 'ОШИБОЧКА'
        
        if len(login) > 32 and len(login) < 5:
            return 'ОШИБОЧКА'
        
        if len(name) > 32 and len(name) < 3:
            return 'ОШИБОЧКА'
        
        if len(password) < 6:
            return 'ОШИБОЧКА'
        
        query = """INSERT INTO users (login, password, email, reg_data, name, birthday)
                   VALUES ('%s', '%s', '%s', '1993-12-12', '%s', '%s')""" % (login, password, email, );
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
