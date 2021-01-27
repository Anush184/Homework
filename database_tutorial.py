import sqlite3
from sqlite3 import Error
import os
import json


database = os.path.join(os.getcwd(), "film.db")
try:
	conn = sqlite3.connect(database)
	print("Connection successfully finished")
except Error as e:
	print(e)

curs = conn.cursor()

#Find the names of movies which name starts with “B”

curs.execute("SELECT title FROM film WHERE title like 'B%'")
for row in curs:
	print(row[0])

#Find the movie which duration is the largest from film table

result = curs.execute("SELECT film_id, title, MAX(length) FROM film").fetchall()
for row in result:
	print(F"film_id: {row[0]}, film title: {row[1]}, largest duration: {row[2]}")

#Write the data from film table into a json file

data = curs.execute("SELECT * FROM film").fetchall()

data_dict = {}
for i in range(1, len(data) + 1):
	dic = dict()
	dic['film_id'] = data[i - 1][0]
	dic['title'] = data[i - 1][1]
	dic['description'] = data[i - 1][2]
	dic['release_year'] = data[i - 1][3]
	dic['rate'] = data[i - 1][4]
	dic['length'] = data[i - 1][5]
	dic['special_features'] = data[i - 1][6]
	data_dict.setdefault(i, dic)

filepath = os.path.join(os.getcwd(), "database.json)")
with open(filepath, "w") as file:
	json.dump(data_dict, file, indent=4, sort_keys=False)

with open("database.json", "r") as file:
	print(file.read())

selected_films = curs.execute("""SELECT * FROM film WHERE release_year > 2010 
And rate BETWEEN 3 AND 5 """).fetchall()

curs.close()
conn.close()

'''
Write script which finds all the movies from film table
which release date is above 2010 and rate is between 3 and 5, 
after that writes them in a new table called filtered_film.
'''

database2 = os.path.join(os.getcwd(), "filtered_film.db")
try:
	con = sqlite3.connect(database2)
	print("Connection successfully finished")
except Error as e:
	print(e)

cursor = con.cursor()
project_query = """ CREATE TABLE IF NOT EXISTS filtered_film(
                                         film_id integer,
                                         title text,
                                         description text,
                                         release_year integer,
                                         rate float,
                                         length integer,
                                         special_features char    
                                         ); """

cursor.execute(project_query)
con.commit()


def insert_function_film(value):
	insert_query = """INSERT INTO filtered_film(film_id, title, description, 
	release_year, rate, length, special_features)VALUES(?, ?, ?, ?, ?, ?, ?);"""
	cursor.execute(insert_query, value)
	con.commit()


for row in selected_films:
	insert_function_film(row)

cursor.close()
con.close()