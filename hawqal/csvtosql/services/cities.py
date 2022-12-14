import csv
from hawqal.dal.dao import connection
from hawqal.migration.schemas import schema

connection.connect
db_cursor = connection.connect.cursor()


class city:

    def cityDB(filepath):
        # cities data to database
        with open(filepath, 'r', encoding="utf8") as file:
            cities_file_reader = csv.reader(file, delimiter=',')
            next(cities_file_reader, None)

            db_cursor

            db_cursor.execute(schema.City_Table)
            for row in cities_file_reader:
                InsertQuery = f'INSERT INTO cities VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}")'
                db_cursor.execute(InsertQuery)

            connection.connect.commit()
