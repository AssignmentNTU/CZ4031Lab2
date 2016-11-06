import psycopg2
#option 2 using PyGreSql

class DatabasePostgresql:


    def __init__(self,dbName,dbUser,dbPassword):
        try:
            self.conn = psycopg2.connect(database=dbName,user=dbUser,password=dbPassword,host="localhost",port=5432)
        except:
            self.conn = None
            print "I am unable to connect to the database"


    

    def closeDatabase(self):
        self.conn.close();
