import mysql.connector
from mysql.connector import Error
try :
    connection= mysql.connector.connect(host='127.0.0.1',user='root',password='',database='sample')
    if connection.is_connected() :
        db_Info = connection.get_server_info()
        print("connected to Mysql database..mysql server version on", db_Info)

        cursor=connection.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("your are connected to -",record)

except Error as e :
    print("Error connecting to mysql",e)
finally :
    #closing connection
    if (connection.is_connected()) :
        cursor.close()
        connection.close()
        print("connection closed")