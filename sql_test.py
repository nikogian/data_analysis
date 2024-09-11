import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

# Run a SQL query
cursor.execute("SELECT * FROM properties LIMIT 5;")
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close the connection
conn.close()
