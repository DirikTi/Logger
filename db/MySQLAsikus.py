import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

STARTUP_SQL_PATH = './startup.sql'

class MySQLAsikus:
    
    def __init__(self) -> None:
        print("in")
        try:
            """
            self.con = mysql.connector.connect(
                host = _host,
                user = _user,
                password = _password,
                database = _database,
                auth_plugin="mysql_native_password"
            )
            """
            load_dotenv()

            self.con = mysql.connector.connect(
                host = os.getenv('MYSQL_HOST'),
                user = os.getenv('MYSQL_USER'),
                password = os.getenv('MYSQL_PASSWORD'),
                database = os.getenv('MYSQL_PASSWORD'),
                auth_plugin="mysql_native_password"
            )
            if self.con.is_connected():
                print("Success Connect")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def startup(self):
        file = open(STARTUP_SQL_PATH, "r")

        startup_query = file.read() 
        
        __cursor = self.con.cursor()

        __cursor.execute(startup_query)
    
    
    def insert(self, query, val) -> bool:
        if(type(query) != str):
            print("Query should be STR")
            return False
            #raise TypeError("Query should be STR")

        try:
            __cursor = self.con.cursor()

            result = __cursor.execute(query, val)

            if(result):
                print("MSG: INSERTED DATA")
            else:
                print("")

        except mysql.connector.Error as err:
            print(err)
    

    def execute(self, query):
        if(type(query) != str):
            print("ERROR: QUERY IS NOT STR %s", query)
            raise TypeError("QUERY IS NOT STR", query)
        
        result = self.cursor.execute(query)

        return result
    
AsikusMysql = MySQLAsikus()