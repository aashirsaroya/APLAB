import sqlite3 as s
conn = s.connect('mydb.db')
print('Opened Database successfully')
conn.execute('''CREATE TABLE IF NOT EXISTS STUDENT(
ID INT PRIMARY KEY,
NAME TEXT NOT NULL,
AGE TEXT NOT NULL,
HOSTEL TEXT,
ROOMNO TEXT
)''')
print("Table created successfully")
conn.execute('''INSERT INTO STUDENT(ID,NAME,AGE,HOSTEL,ROOMNO)
VALUES(12,'AASHIR','20','14','1130')
''')
conn.execute('''INSERT INTO STUDENT(ID,NAME,AGE,HOSTEL,ROOMNO)
VALUES(21,'ARAVIND','20','15','130')
''')
conn.execute('''INSERT INTO STUDENT(ID,NAME,AGE,HOSTEL,ROOMNO)
VALUES(31,'ARYAN','20','15','830')
''')
print('After inserting')
c = conn.execute('''Select id,name,age,hostel,roomno from student ''')
for row in c:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
conn.execute('''DELETE FROM STUDENT where ID = 2''')
conn.commit()
c = conn.execute('''Select id,name,age,hostel,roomno from student ''')
for row in c:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
print('Operation Success:)')
conn.execute('''UPDATE STUDENT
                SET AGE = '19'
                WHERE ID = 1
''')
conn.commit()
c = conn.execute('''Select id,name,age,hostel,roomno from student ''')
for row in c:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
print('Operation Success Again:) ')
