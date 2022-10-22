

from bottle import default_app, route

import sqlite3

connection = sqlite3.connect("shopping_list.db");

@route('/')
def hello_world():
    return 'Hello from ADITYA Gotlur(811229613)!'

@route('/shopingList')
def get_list():
    cursor = connection.cursor()
    data = cursor.execute("select * from  list")
    data = list(data)
    data = [ {'id': da[0] , 'des': da[1] }  for da in data ]
    return "List of shopping items:", str(data)

application = default_app()
