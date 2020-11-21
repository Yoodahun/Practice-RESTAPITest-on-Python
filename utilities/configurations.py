import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


def getSQLConnection():
    connection_data = getConfig()['SQL']

    try:
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
