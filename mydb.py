import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mounirbarakaidol',
    auth_plugin='mysql_native_password'
    )
# prepare a cursor object
cursorObject = dataBase.cursor()
#create a databse
cursorObject.execute('CREATE DATABASE db_crm')

print("all done")