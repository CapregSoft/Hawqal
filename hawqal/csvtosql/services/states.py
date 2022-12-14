import csv
from hawqal.dal.dao import connection
from hawqal.migration.schemas import schema

connection.connect
db_cursor = connection.connect.cursor()


class state:

    def stateDB(filepath):
        # states data to database
        with open(filepath, 'r', encoding="utf8") as file:
            states_file_reader = csv.reader(file, delimiter=',')
            next(states_file_reader, None)

            db_cursor

            db_cursor.execute(schema.State_Table)
            for row in states_file_reader:
                InsertQuery = f'INSERT INTO states VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}")'
                db_cursor.execute(InsertQuery)

            connection.connect.commit()
