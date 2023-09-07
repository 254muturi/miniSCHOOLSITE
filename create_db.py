# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="daniel1st$mwangi",
#     database="FadhiliDB"  # Add the database name here
# )
#
# my_cursor = mydb.cursor()
#
# my_cursor.execute("CREATE DATABASE FadhiliDB")
#
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)
import mysql.connector

# Replace with your database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "daniel1st$mwangi",
    "database": "FadhiliDB",
}

# Connect to the database
connection = mysql.connector.connect(**db_config)

# Create a cursor
cursor = connection.cursor()

# Execute an SQL query
query = "SELECT * FROM FadhiliDB"
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
