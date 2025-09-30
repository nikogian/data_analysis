import mysql.connector
import pandas as pd

# MySQL connection configuration
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = connection.cursor()

# Step 1: Create a new database (if it doesn't exist)
db_name = 'sql_real_estate'
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
connection.commit()

# Switch to the new database
connection.database = db_name

# Step 2: Load CSV data
data = pd.read_csv('uae_real_estate_2024.csv')

# Truncate long strings in description values and Nan Values
data['description'] = data['description'].apply(lambda x: x[:250] if isinstance(x, str) else x)
data = data.where(pd.notnull(data), None)

# Step 3: Dynamically create table SQL based on CSV headers
table_name = 'properties'
columns = ', '.join([f'{col} VARCHAR(255)' for col in data.columns])  # Modify column types as needed
create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});'
cursor.execute(create_table_sql)

# Step 4: Insert CSV data into the table
for index, row in data.iterrows():
    sql = f"INSERT INTO {table_name} ({', '.join(data.columns)}) VALUES ({', '.join(['%s'] * len(row))})"
    cursor.execute(sql, tuple(row))

connection.commit()

connection.close()

print(f"Database {db_name} and table {table_name} created, and data has been successfully inserted.")

