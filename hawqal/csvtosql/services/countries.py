import csv


class Country:
    def __init__(self, databaseConn, schema, CsvfilePath):
        self.databaseConn = databaseConn
        self.schema = schema
        self.CsvfilePath = CsvfilePath

    def countryDB(self):
      # countries data to database
        with open(self.CsvfilePath, 'r', encoding="utf8") as file:
            countries_file_reader = csv.reader(file, delimiter=',')
            next(countries_file_reader, None)

            cursor = self.databaseConn.cursor()

            cursor.execute(self.schema)
            # connection.cursor.execute(schema.Country_Table)
            for row in countries_file_reader:
                InsertQuery = f'INSERT INTO countries VALUES ("{row[0]}","{row[1]}","{"+"+row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}","{row[13]}","{row[14]}")'
                cursor.execute(InsertQuery)

            self.databaseConn.commit()
