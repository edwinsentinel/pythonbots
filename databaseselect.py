import mysql.connector
from mysql.connector import Error
try :
    mySQLconnection= mysql.connector.connect(host='127.0.0.1',user='root',password='',database='sample')

    sql_select_Query = "select * from python_developers"
    cursor = mySQLconnection .cursor()
    dbdetails=open("try.xls","w")
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in python_developers is - ", cursor.rowcount)
    dbdetails.write("Printing each row's column values i.e.  developer record"+'\n')
    for row in records:
      line=str(row)
      dbdetails.write(line+'\n')
    dbdetails.close()       
    cursor.close()
   


except Error as e :
    print ("Error while connecting to MySQL", e)


finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")