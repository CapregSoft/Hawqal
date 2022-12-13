import csv
import sqlite3

# countries table schema
Country_Table = '''CREATE TABLE if not Exists countries(
      country_id int PRIMARY KEY NOT NULL,
      country_name TEXT NOT NULL
    )
    '''

# states table schema
State_Table = '''CREATE TABLE if not Exists states(
      state_id int PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      country_name TEXT NOT NULL,
      country_id int NOT NULL,
      FOREIGN KEY (country_id) REFERENCES countries (country_id)
    )'''

# cities table schema
City_Table = '''CREATE TABLE if not Exists cities(
  city_id int PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  state_id int NOT NULL,
  country_name TEXT NOT NULL,
  country_id int NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states (state_id),
  FOREIGN KEY (country_id) REFERENCES countries (country_id)
)'''

connection = sqlite3.connect("hawqalDB.sqlite")

# countries data to database
with open("countries.csv", 'r', encoding="utf8") as file:
    countries_file_reader = csv.reader(file, delimiter=',')
    next(countries_file_reader, None)

    cursor = connection.cursor()

    cursor.execute(Country_Table)
    for row in countries_file_reader:
        InsertQuery = f'INSERT INTO countries VALUES ("{row[0]}","{row[1]}")'
        cursor.execute(InsertQuery)

    connection.commit()

# states data to database
with open("states.csv", 'r', encoding="utf8") as file:
    states_file_reader = csv.reader(file, delimiter=',')
    next(states_file_reader, None)

    cursor = connection.cursor()

    cursor.execute(State_Table)
    for row in states_file_reader:
        InsertQuery = f'INSERT INTO states VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}")'
        cursor.execute(InsertQuery)

    connection.commit()

# cities data to database
with open("cities.csv", 'r', encoding="utf8") as file:
    cities_file_reader = csv.reader(file, delimiter=',')
    next(cities_file_reader, None)

    cursor = connection.cursor()

    cursor.execute(City_Table)
    for row in cities_file_reader:
        InsertQuery = f'INSERT INTO cities VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}")'
        cursor.execute(InsertQuery)

    connection.commit()

connection.close()
