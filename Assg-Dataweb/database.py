import sqlite3

connection = sqlite3.connect("shopping_list.db");

def get_items():
    cursor = connection.cursor()
    data = cursor.execute("select id, description from  list")
    data = list(data)
    data = [ {'id': da[0] , 'des': da[1] }  for da in data ]
    return data

def add_funFoodItem(description):
    cursor=connection.cursor()
    cursor.execute(f"insert into list(description) values ('{description}')")
    connection.commit()

def delet_item(id):
    cursor=connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()

def update(id,description):
    cursor=connection.cursor()
    cursor.execute(f"update list set description='{description}' where id={id}")
    connection.commit()