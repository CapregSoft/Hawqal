from hawqal.dal.dao import Database
from .services.countries import Country
from .services.states import State
from .services.cities import City
from hawqal.migration.schemas import Schema


class Convert:
    def __init__(self):
        try:
            self.database = Database(
                'database\hawqalDB.sqlite').makeConnection()
            print("Database Connected Sucessfully")
        except:
            print('Database Connection Error')
        self.CitySchema = Schema().getCitySchema()
        self.StateSchema = Schema().getStateSchema()
        self.CountriesSchema = Schema().getCountrySchema()

    def csv_to_sql(self):
        print('Converting your data from CSV to SQlite Database...')
        try:
            countryObj = Country(
                self.database, self.CountriesSchema, 'hawqal\data\countries.csv')
            countryObj.countryDB()

            stateObj = State(self.database, self.StateSchema,
                             'hawqal\data\states.csv')
            stateObj.stateDB()

            cityObj = City(self.database, self.CitySchema,
                           'hawqal\data\cities.csv')
            cityObj.cityDB()

            self.database.commit()
            print("Data converted Sucessfully")
        except:
            print("error while converting data")
