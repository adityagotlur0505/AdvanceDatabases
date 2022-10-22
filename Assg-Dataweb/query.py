import sqlite3


connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

data = cursor.execute("select * from  list")

data = list(data)

print (data)

