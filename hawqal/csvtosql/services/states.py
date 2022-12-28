import csv


class State:
    def __init__(self, databaseConn, schema, CsvfilePath):
        self.databaseConn = databaseConn
        self.schema = schema
        self.CsvfilePath = CsvfilePath

    def stateDB(self):
        # states data to database
        with open(self.CsvfilePath, 'r', encoding="utf8") as file:
            states_file_reader = csv.reader(file, delimiter=',')
            next(states_file_reader, None)

            cursor = self.databaseConn.cursor()
            cursor.execute(self.schema)
            for row in states_file_reader:
                InsertQuery = f'INSERT INTO states VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}")'
                cursor.execute(InsertQuery)

            self.databaseConn.commit()
