import mysql.connector
from utilities.JSON_converter import convert_to_json
from access_db import *

def connect_to_database():
    try:
        mydb_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        return mydb_connection
    except:
        print("Error connection to database")

def fetchall(sql_statement, attributes = None):
    try:
        connection = connect_to_database()
        cur = connection.cursor(dictionary=True)
        cur.execute(sql_statement, attributes)
        res = cur.fetchall()
        res = convert_to_json(res)
        return res
    except:
        raise ValueError('Error while fetching data from database.')
    finally:
        cur.close()
    
def fetchone(sql_statement, attributes):
    try:
        connection = connect_to_database()
        cur = connection.cursor(dictionary=True)
        cur.execute(sql_statement, attributes)
        res = cur.fetchone()
        res = convert_to_json(res)
        return res
    except:
        raise ValueError('Error while fetching data from database.')
    finally:
        cur.close()

def insertone(sql_statment, attributes):
    try:
        connection = connect_to_database()
        cur = connection.cursor()
        cur.execute(sql_statment, attributes)
        connection.commit()
        print(f'Successfull inserting person: {attributes["Lastname"]}, {attributes["Firstname"]}')
        return True
    except:
        raise ValueError(f'Error while inserting person: {attributes["Lastname"]}, {attributes["Firstname"]}')
    finally:
        cur.close()