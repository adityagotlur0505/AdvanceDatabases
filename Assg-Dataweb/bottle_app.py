

from bottle import default_app, route, template

import sqlite3

connection = sqlite3.connect("shopping_list.db");

@route('/')
def hello_world():
    return 'Hello from ADITYA Gotlur(811229613)!'

@route('/shopingList')
def get_list():
    cursor = connection.cursor()
    data = cursor.execute("select id, description from  list")
    data = list(data)
    data = [ {'id': da[0] , 'des': da[1] }  for da in data ]
    return template("list_items.tpl" , name="aditya Richard" , shopping_List=data)

application = default_app()
