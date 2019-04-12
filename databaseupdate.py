import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try :
     conn= mysql.connector.connect(host='127.0.0.1',user='root',password='',database='computers')

     cursor = conn.cursor()
     dbdetails=open("update.txt","w")
     dbdetails.write("Before updating record ")
     sql_select_query = """select * from computers where id = 14"""
     cursor.execute(sql_select_query)
     record = cursor.fetchone()
     print (record)
     line=str(record)
     dbdetails.write(line+'\n')
     #Update single record now
     sql_update_query = """Update computers set processor = 35 where id = 14"""
     cursor.execute(sql_update_query)
     conn.commit()
     print ("Record Updated successfully ")

     print("After updating record ")
     dbdetails.write("After updating record ")
     cursor.execute(sql_select_query)
     record = cursor.fetchone()
     print(record)
     line=str(record)
     dbdetails.write(line+'\n')
except mysql.connector.Error as error :
    print("Failed to update record to database: {}".format(error))
    conn.rollback()
finally:
    #closing database connection.
    if(conn.is_connected()):
        conn.close()
        print("connection is closed")