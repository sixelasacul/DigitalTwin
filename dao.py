import sqlite3
from config import config

db_file = config['db']


class DAO:
    def __init__(self):
        self.connection = None
        self.last_date_time_value = 0
        self.table_count = 0

    def init_db_cursor(self):
        if self.connection is None:
            self.connection = sqlite3.connect(db_file)
        return self.connection.cursor()

    def retrieve_table_length(self):
        print("Retrieving table length")
        cursor = self.init_db_cursor()
        query = "select count(valuedatetime) from temperatures;"
        cursor.execute(query)
        count = cursor.fetchone()
        cursor.close()
        self.table_count = count[0]
        print("Retrieved length : ", count[0])
        return count[0]

    def retrieve_temperatures(self):
        print("Retrieving temperatures for following datetime : %s" % self.last_date_time_value)
        values = []
        try:
            cursor = self.init_db_cursor()
            query = "select min(valuedatetime), salle1, salle2, salle3, salle4 from temperatures where valuedatetime " \
                    "> '%s' order by valuedatetime;" % self.last_date_time_value
            cursor.execute(query)
            register = cursor.fetchone()
            cursor.close()

            if register[0] is None:
                print("finished")
            else:
                self.last_date_time_value = register[0]
                for i in range(1, 5):
                    values.append(int(register[i]))
        except Exception as e:
            print("Unexpected error:", e)
            raise e
        finally:
            print("Retrieved values : ", str(values))
            return values
