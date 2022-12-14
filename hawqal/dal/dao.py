import sqlite3
import os


class connection:
    if os.path.exists("database\hawqalDB.sqlite"):
        os.remove("database\hawqalDB.sqlite")
    connect = sqlite3.connect("database/hawqalDB.sqlite")
