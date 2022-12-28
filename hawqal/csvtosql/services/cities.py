import csv


class City:
    def __init__(self, databaseConn, schema, CsvfilePath):
        self.databaseConn = databaseConn
        self.schema = schema
        self.CsvfilePath = CsvfilePath

    def cityDB(self):
        # cities data to database
        with open(self.CsvfilePath, 'r', encoding="utf8") as file:
            cities_file_reader = csv.reader(file, delimiter=',')
            next(cities_file_reader, None)

            cursor = self.databaseConn.cursor()

            cursor.execute(self.schema)
            for row in cities_file_reader:
                InsertQuery = f'INSERT INTO cities VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}")'
                cursor.execute(InsertQuery)
            self.databaseConn.commit()
