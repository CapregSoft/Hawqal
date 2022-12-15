import sqlite3
import os


class Database:
    def __init__(self, path):
        self.databasePath = path

    def makeConnection(self):
        if os.path.exists(f"{self.databasePath}"):
            os.remove(f"{self.databasePath}")
        return sqlite3.connect(f"{self.databasePath}")
