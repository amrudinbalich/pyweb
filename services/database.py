import mysql.connector
from mysql.connector.connection import MySQLConnection


def database_connect() -> MySQLConnection:
    """
        Create a connection to the MySQL database.

        Returns:
            A MySQLConnection object if the connection succeeds,
            otherwise None.
        """

    return mysql.connector.connect(
        user='root',
        host='localhost',
        password='',
        database='pyweb'
    )