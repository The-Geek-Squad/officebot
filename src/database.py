import mysql.connector
from src.settings import HOST, USER, PASSWORD, DATABASE


class Database:
    def __init__(self):
        self._conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWORD,
            database=DATABASE)
        self._cursor = self._conn.cursor(dictionary=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


if __name__ == '__main__':
    test = Database()
    query = test.query("SHOW DATABASES")
    print(type(query))
    print(query[0]['Database'])
