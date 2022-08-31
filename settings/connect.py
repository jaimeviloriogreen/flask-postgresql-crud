import psycopg2
from .credentials import dataConnection

class Connect:
    def getConnect(self):
        conn = psycopg2.connect(
            host = dataConnection["host"],
            dbname = dataConnection["dbname"],
            user = dataConnection["user"],
            password = dataConnection["password"],
            port = dataConnection["port"]
        )
        return conn