import main
import mysql.connector
class Dba:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

dbaname = Dba(main.hostname, main.username, main.passw, main.datab)


mydb = mysql.connector.connect(
    host= dbaname.host,
    user= dbaname.user,
    password= dbaname.password,
    database= dbaname.database
)

def insert_stock():
    mycursor = mydb.cursor()
    sql = "INSERT INTO testTable (testMonth, testOpen, testHigh, testLow, testClose, testVolume) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (main.month, main.avgMonth['1. open'], main.avgMonth['2. high'], main.avgMonth['3. low'], main.avgMonth['4. close'], main.avgMonth['5. volume'])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

insert_stock()





