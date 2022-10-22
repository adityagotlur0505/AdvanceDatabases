import sqlite3

#Establish a connection with sqlite3

connection = sqlite3.connect("shopping_list.db");

#create a cursor to handle query executions

cursor = connection.cursor()

#drop tables if there are any related to pets and and species

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Biriyani')")
cursor.execute("insert into list (description) values ('Tandoori Chichen')")
cursor.execute("insert into list (description) values ('Toor Dal')")
cursor.execute("insert into list (description) values ('Milk')")
cursor.execute("insert into list (description) values ('Eggs')")

#commit the statements close connection
connection.commit()
connection.close()

print("executed shopping list")

