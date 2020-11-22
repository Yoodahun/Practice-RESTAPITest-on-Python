import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


def getSQLConnection():


    try:
        connection_data = getConfig()['SQL']
        sql_connection = mysql.connector.connect(
            host=connection_data['host'],
            database=connection_data['database'],
            user=connection_data['user'],
            password=connection_data['password']
        )
        if sql_connection.is_connected():
            print("Connection Successful")
            return sql_connection
    except Error as e:
        print(e)


def getQuery(query):

    connection_data = getSQLConnection()
    cursor = connection_data.cursor()
    cursor.execute(query)
    result_db = cursor.fetchone()
    connection_data.close()
    return result_db