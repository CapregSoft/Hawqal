import csv
from dal.dao import connection
from migration.schemas import schema

connection.connect
db_cursor = connection.connect.cursor()


class read:

    # countries data to database
    with open("countries.csv", 'r', encoding="utf8") as file:
        countries_file_reader = csv.reader(file, delimiter=',')
        next(countries_file_reader, None)

        db_cursor

        db_cursor.execute(schema.Country_Table)
        # connection.cursor.execute(schema.Country_Table)
        for row in countries_file_reader:
            InsertQuery = f'INSERT INTO countries VALUES ("{row[0]}","{row[1]}")'
            db_cursor.execute(InsertQuery)

        connection.connect.commit()

    # states data to database
    with open("states.csv", 'r', encoding="utf8") as file:
        states_file_reader = csv.reader(file, delimiter=',')
        next(states_file_reader, None)

        db_cursor

        db_cursor.execute(schema.State_Table)
        for row in states_file_reader:
            InsertQuery = f'INSERT INTO states VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}")'
            db_cursor.execute(InsertQuery)

        connection.connect.commit()

    # cities data to database
    with open("cities.csv", 'r', encoding="utf8") as file:
        cities_file_reader = csv.reader(file, delimiter=',')
        next(cities_file_reader, None)

        db_cursor

        db_cursor.execute(schema.City_Table)
        for row in cities_file_reader:
            InsertQuery = f'INSERT INTO cities VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}")'
            db_cursor.execute(InsertQuery)

        connection.connect.commit()

    connection.connect.close()
