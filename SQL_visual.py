import pandas as pd
import matplotlib as plt
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host="localhost",        # Server address (use 'localhost' for local database)
            user="root",    # MySQL username (e.g., 'root')
            password="21317",# MySQL password
            database="mysql_real_estate" # The name of the database you want to connect to
        )
        
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to MySQL")
        return None

# Connect to the database
db_connection = create_connection()


with open('SQL_edit.sql', 'r') as file:
    query = file.read()

df_query = pd.read_sql_query(query, db_connection)


# Remember to close the connection when done
if db_connection:
    db_connection.close()

