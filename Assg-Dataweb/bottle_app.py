

from bottle import default_app, route, get, post, template, request, redirect

import sqlite3

import database

connection = sqlite3.connect("shopping_list.db");




@route('/')
def hello_world():
    redirect('/shopingList')

@route('/shopingList')
def get_list():
    #cursor = connection.cursor()
    #data = cursor.execute("select id, description from  list")
    #data = list(data)
    #data = [ {'id': da[0] , 'des': da[1] }  for da in data ]
    data=database.get_items()
    return template("list_items.tpl" , name="aditya Richard" , shopping_List=data)

@get('/addFood')
def post_list():
    return template("add_food.tpl")

@post('/addFood')
def submit_pressFun():

    description=request.forms.get('description')
    database.add_funFoodItem(description)
    #cursor=connection.cursor()
    #cursor.execute(f"insert into list(description) values ('{description}')")
    #connection.commit()
    redirect('/shopingList')

@route("/delete/<id>")
def get_delete(id):
    database.delet_item(id)
    #cursor=connection.cursor()
    #cursor.execute(f"delete from list where id={id}")
    #connection.commit()
    redirect('/shopingList')

@get("/edit/<id>")
def get_edit(id):
    cursor=connection.cursor()
    items=cursor.execute(f"select description from list where id={id}")
    items=list(items)
    if len(items) != 1:
        redirect('/shopingList')
    description=items[0][0]
    return template("edit_shopping.tpl", id=id, description=description)
    #return f"we want to edit {description} for the item{id}"

@post("/edit/<id>")
def edit_item(id):
    description=request.forms.get('description')
    database.update(id,description)
    redirect('/shopingList')

application = default_app()
