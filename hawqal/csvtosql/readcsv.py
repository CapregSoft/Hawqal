from hawqal.dal.dao import connection
from .services.countries import country
from .services.states import state
from .services.cities import city

connection.connect
db_cursor = connection.connect.cursor()


class convert:

    def csv_to_sql():
        country.countryDB("hawqal/data/countries.csv")
        state.stateDB("hawqal/data/states.csv")
        city.cityDB("hawqal/data/cities.csv")

        connection.connect.close()
