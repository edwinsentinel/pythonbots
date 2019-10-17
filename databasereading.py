import mysql.connector
from mysql.connector import Error


def database_connector(host_name, username, password, schema):
    """
    connects to a database used the passed parameters
    :param host_name: the server to which the database is installed
    :param username: the username who is logging into the database
    :param password: the password for authenticating the user
    :param schema: the database that we wish to connect to
    """
    try:
        connection = mysql.connector.connect(host=host_name, user=username, password=password, database=schema)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("connected to Mysql database..mysql server version on", db_Info)

            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("your are connected to -", record)
    except Error as e:
        print("Error connecting to mysql", e)
    finally:
        # closing connection
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("connection closed")
