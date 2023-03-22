import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    port = 3307,
    database = 'azarfoods'
)
mycursor = mydb.cursor()