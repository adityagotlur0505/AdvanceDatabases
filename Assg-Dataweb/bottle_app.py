

from bottle import default_app, route, get, post, template, request, redirect

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

@get('/addFood')
def post_list():
    return template("add_food.tpl")

@post('/addFood')
def submit_pressFun():
    description=request.forms.get('description')
    cursor=connection.cursor()
    cursor.execute(f"insert into list(description) values ('{description}')")
    connection.commit()
    redirect('/shopingList')

@route("/delete/<id>")
def get_delete(id):
    cursor=connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()
    redirect('/shopingList')

application = default_app()
