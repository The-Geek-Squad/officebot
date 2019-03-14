import mysql.connector
from src import settings


def main():
    mydb = mysql.connector.connect(
        host=settings.HOST,
        user=settings.USER,
        passwd=settings.PASSWORD)
    cursor = mydb.cursor()

    # Create Database if doesn't exist
    sql = "CREATE DATABASE IF NOT EXISTS " + settings.DATABASE
    cursor.execute(sql)

    # Set Database
    sql = "USE " + settings.DATABASE
    cursor.execute(sql)

    # Drop Table if Exist
    sql = "DROP TABLE IF EXISTS quotes"
    cursor.execute(sql)

    # Create Table Quotes
    sql = """CREATE TABLE quotes (
    id INT NOT NULL AUTO_INCREMENT, 
    quote TEXT NOT NULL, 
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP, 
    date_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id))"""
    cursor.execute(sql)


if __name__ == '__main__':
    main()
