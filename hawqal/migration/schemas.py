class Schema:
    def __init__(self):
        # countries table schema
        self.Country_Table = '''CREATE TABLE if not Exists countries(
        country_name TEXT PRIMARY KEY NOT NULL,
        iso_code TEXT NOT NULL,
        phone_code TEXT NOT NULL,
        capital TEXT NOT NULL,
        currency TEXT NOT NULL,
        currency_name TEXT NOT NULL,
        currency_symbol TEXT NOT NULL,
        country_domain TEXT NOT NULL,
        region TEXT NOT NULL,
        subregion TEXT NOT NULL,
        timezone TEXT NOT NULL,
        zone_city TEXT NOT NULL,
        UTC TEXT NOT NULL,
        latitude TEXT NOT NULL,
        longitude TEXT NOT NULL
      )
      '''

    # states table schema
        self.State_Table = '''CREATE TABLE if not Exists states(
          state_id int PRIMARY KEY NOT NULL,
          state_name TEXT NOT NULL,
          country_name TEXT NOT NULL,
          latitude TEXT NOT NULL,
          longitude TEXT NOT NULL,
          FOREIGN KEY (country_name) REFERENCES countries (country_name)
          )'''

    # cities table schema
        self.City_Table = '''CREATE TABLE if not Exists cities(
          city_id int PRIMARY KEY NOT NULL,
          city_name TEXT NOT NULL,
          state_name TEXT NOT NULL,
          state_id int NOT NULL,
          country_name TEXT NOT NULL,
          latitude TEXT NOT NULL,
          longitude TEXT NOT NULL,
          FOREIGN KEY (state_id) REFERENCES states (state_id),
          FOREIGN KEY (country_name) REFERENCES countries (country_name)
          )'''

    def getCitySchema(self):
        return self.City_Table

    def getStateSchema(self):
        return self.State_Table

    def getCountrySchema(self):
        return self.Country_Table
