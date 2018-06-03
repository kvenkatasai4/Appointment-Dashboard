import psycopg2
import logging


class PostgreSQLCRUD:
    def __init__(self):
        self.host = "localhost"
        self.port = 5433
        self.dbname = "Appointments"
        self.username = "postgres"
        self.password = "1234"
        self.table_name = "Appointments"
        self.cur = 0
        self.conn = 0
        logging.getLogger().setLevel(logging.DEBUG)

    def connect(self):
        try:
            logging.info("Connecting to Database: {}".format(self.dbname))
            self.conn = psycopg2.connect(host=self.host, port=self.port, dbname=self.dbname,
                                         user=self.username, password=self.password)
            self.cur = self.conn.cursor()
            logging.info("Connecting to Database: {} successful".format(self.dbname))
            result = True
        except Exception as error:
            logging.error("Connecting to Database: {} failed with error: {}".format(self.dbname, error))
            raise error
        return result

    def close(self):
        try:
            logging.info("Closing cursor to Database: {}".format(self.dbname))
            self.cur.close()
            logging.info("Closing connection to Database: {}".format(self.dbname))
            self.conn.close()
            result = True
        except Exception as error:
            logging.error("Error: {} while closing connecting to Database: {}".format(error, self.dbname))
            raise error
        return result

    def read_all(self):
        try:
            self.cur.execute('select * from "Appointments"')
            records = self.cur.fetchall()
            list_json = []
            for record in records:
                list_json.append({"description": record[0], "date": record[1], "time": record[2]})
        except Exception as error:
            logging.error("Error in reading data: {}".format(error))
            raise error
        return list_json

    def read_query(self, value):
        try:
            self.cur.execute('select * from "Appointments" where description like \'%' + value + '%\'')
            records = self.cur.fetchall()
            list_json = []
            for record in records:
                list_json.append({"description": record[0], "date": record[1], "time": record[2]})
        except Exception as error:
            logging.error("Error in executing Query: {}".format(error))
            raise error
        return list_json

    def insert_record(self, description=None, date=None, time=None):
        try:
            if description:
                self.cur.execute('INSERT INTO "Appointments"(description, date, time) VALUES '
                                 '(\'' + description +'\', \'' + date +'\', \'' + time +'\')')
                self.conn.commit()
                result = True
            else:
                raise Exception("Invalid value")
        except Exception as error:
            logging.error("Error in inserting record: {}".format(error))
            raise error
        return result

if __name__ == "__main__":
    db = PostgreSQLCRUD()
    db.connect()
    # db.insert_record("test hello")
    # print(db.read_all())
    print(db.read_query("test"))
    db.close()
