import csv
from hawqal.dal.dao import connection
from hawqal.migration.schemas import schema

connection.connect
db_cursor = connection.connect.cursor()


class country:

    def countryDB(filepath):
      # countries data to database
        with open(filepath, 'r', encoding="utf8") as file:
            countries_file_reader = csv.reader(file, delimiter=',')
            next(countries_file_reader, None)

            db_cursor

            db_cursor.execute(schema.Country_Table)
            # connection.cursor.execute(schema.Country_Table)
            for row in countries_file_reader:
                InsertQuery = f'INSERT INTO countries VALUES ("{row[0]}","{row[1]}")'
                db_cursor.execute(InsertQuery)

            connection.connect.commit()
