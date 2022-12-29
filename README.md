# Hawqal CSV Data Import

This package provides a utility for importing data from CSV files into a Hawqal database.

## Installation

To install the package, run the following command:


## Usage

To use the package, you will need to provide a connection string to your Hawqal database, as well as the path to the CSV file you want to import.

Here is an example of how to import data from a CSV file:

```python
from hawqal_csv_import import import_csv

connection_string = "host=myhost port=5432 dbname=mydatabase user=myuser password=mypassword"
csv_file_path = '/path/to/my/csv/file.csv'

import_csv(connection_string, csv_file_path)
```

I hope this helps! Let me know if you have any questions or need any further assistance.
