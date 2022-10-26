import sqlite3


connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

data = cursor.execute("select id, description from  list")

data = list(data)

print (data)

data = [ {'id': da[0] , 'des': da[1] }  for da in data ]

print (data)


