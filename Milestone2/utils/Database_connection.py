import sqlite3
# C
class DataBaseConnection:
    
    def __init__(self, host):
        self.connection = None
        self.host = host
    def __enter__(self):
        self.connection =  sqlite3.connect(self.host)
        return self.connection
    def __exit__(self, exc_type, exc_val, exc_tb): # Database could be left in an inconsistant state. 
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

