import sqlite3

connection = sqlite3.connect('pets.db')

cursor = connection.cursor()

cursor.execute("delete from pet where species_id == 3")
connection.commit()
print("updated")
rows = cursor.execute(" select name, kind from pet,species where pet.species_id=species.id")

rows = list(rows)

for row in rows:
    name,kind=row
    print(f"my {kind} is named as {name}.")