import sqlite3

#Establish a connection with sqlite3

connection = sqlite3.connect("pets.db");

#create a cursor to handle query executions

cursor = connection.cursor()

#drop tables if there are any related to pets and and species

try:
    cursor.execute("drop table pet")
except:
    pass

try:
    cursor.execute("drop table species")
except:
    pass

cursor.execute("create table pet (id integer primary key, name text, species_id int)")
cursor.execute("create table species(id integer primary key, kind text)")
cursor.execute("insert into species (kind) values ('dog')")
cursor.execute("insert into species (kind) values ('dinasour')")
cursor.execute("insert into species (kind) values ('croc')")

cursor.execute("insert into pet(species_id, name) values (1, 'Manohar')")
cursor.execute("insert into pet(species_id, name) values (2, 'Vishal')")
cursor.execute("insert into pet(species_id, name) values (3, 'Kisses')")

#commit the statements close connection
connection.commit()
connection.close()

print("executed")



