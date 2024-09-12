import pandas as pd
import sqlite3

# Read CSV into a DataFrame
df = pd.read_csv('uae_real_estate_2024.csv')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('real_estate.db')

# Write the data to a SQL table
df.to_sql('properties', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

