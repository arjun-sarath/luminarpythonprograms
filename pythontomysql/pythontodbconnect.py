# mysql-connector

# step 1: import mysql module

import mysql.connector

# step 2: establish connection

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password"
)

# step 3: create cursor object

cursor = db.cursor()

# step 4: execute sql queries

sql = "select version()"
cursor.execute(sql)
data = cursor.fetchone()
print(data)

# step 5: close db connection

