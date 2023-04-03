import sqlite3

conn = sqlite3.connect("employee.db")
print("connected")


conn.execute("INSERT INTO staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES(1,'Angela','Mukami',18,45000.00,'Employer')")

conn.execute("INSERT INTO staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES(2,'Alexa','Grant',19,50000.00,'Employer')")

conn.execute("INSERT INTO staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES(3,'Austin','Mutugi',20,55000.00,'Employer')")

conn.execute("INSERT INTO staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES(4,'Albert','Muchangi',21,60000.00,'Employer')")

conn.commit()
print("Inserted values successfully")
conn.close()