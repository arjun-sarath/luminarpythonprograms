import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="mydb",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

# sql = "create table employee(eid int,name varchar(50),desig varchar(50),salary int)"
# cursor.execute(sql)
# db.close()

# sql = "insert into employee(eid,name,desig,salary) values(100,'ajay','developer',25000)"
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e.args)
#     db.rollback()
# finally:
#     db.close()

# sql = "update employee set eid=101 where name='ajay'"
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e.args)
#     db.rollback()
# finally:
#     db.close()

f = open("employee", "r")
for lines in f:
    data = lines.rstrip("\n").split(",")
    sql = "insert into employee(eid,name,desig,salary) values(%s,%s,%s,%s)"
    try:
        cursor.execute(sql, tuple(data))
        db.commit()
    except Exception as e:
        print(e.args)
        db.rollback()