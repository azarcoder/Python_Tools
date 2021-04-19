import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1538',
    database='pythondbms'
)
mycursor=mydb.cursor() 

#********create database**********
#mycursor.execute('CREATE DATABASE PYTHONDBMS') #CREATE DATABSES

'''#**************show database*************
mycursor.execute('show databases') #show all databases
for i in mycursor:
    print(i)
'''

#************create table*******************
#mycursor.execute('CREATE TABLE STUDENTS(id int,name varchar(255),age int not null)')
'''
mycursor.execute('SHOW TABLES')
for X in mycursor:
    print(X)
'''

#***************ALTER TABLE****************
#mycursor.execute('ALTER TABLE STUDENTS ADD COLUMN COURSE  VARCHAR(30)')

#******INSERT********
#___________SINGLE DATA INSRT__________
'''
sql='INSERT INTO STUDENTS (ID,NAME,AGE,COURSE) VALUES (%s,%s,%s,%s)'
val=('1','azar','19','python')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,'record inserted.')
'''
#___________MULTIPLE DATA INSERT________
'''
sql='INSERT INTO STUDENTS (ID,NAME,AGE,COURSE) VALUES (%s,%s,%s,%s)'
val=[
    ('6','bilal','22','civil'),
    ('2','fabrico','56','python'),
    ('3','vaishnavi','19','python'),
    ('4','faisal','20','dbms'),
    ('5','alisia','23','english')
    ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,'was inserted.')
'''

#************SELECT*************
'''
mycursor.execute('SELECT * FROM STUDENTS')
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''

#SELECTING COLUMN
'''
mycursor.execute('SELECT name,course from STUDENTS')
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''

'''
#fetchone() method
mycursor.execute('SELECT * FROM STUDENTS')
myresult=mycursor.fetchone() #only shows first row (if you want to see next row data! you craete another fetchoone()
myresult=mycursor.fetchone() #it's show second data of the students
print(myresult)
'''

#*************WHERE****************
'''
sql="SELECT * FROM STUDENTS WHERE COURSE='python'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''

#Wildcard character
'''
sql="SELECT * FROM STUDENTS WHERE name like '%a'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''


#*********ORDERBY**********
'''
sql="SELECT * FROM STUDENTS ORDER by name"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''
#desc()
'''
sql="SELECT * FROM STUDENTS ORDER by name DESC"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''

#************DELETE***************
'''
sql="DELETE FROM STUDENTS WHERE NAME='ALISIA'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
mydb.commit()
print(mycursor.rowcount,'record(s) deleted')

'''

#**************UPDATE***********
'''
sql="UPDATE STUDENTS SET NAME='BILAL BILZ' WHERE NAME='BILAL'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'record(s) affected')
'''

#************LIMIT***************
'''
mycursor.execute('select*from students limit 3')
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''

#OFFSET
#start from another position
'''
mycursor.execute('select*from students limit 4 offset 2')
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''
#************DROP TABLE*********
'''
sql='drop table students'
mycursor.execute(sql)
'''

#drop only if Exists
'''
sql='drop table if exists students'
mycursor.execute(sql)
'''

#************JOINS*****************
#mycursor.execute('create table users (id int auto_increment primary key, name varchar(30), fav int)')
#mycursor.execute('create table products (id int, name varchar(255))')
'''
sql='INSERT INTO USERS (ID,NAME,FAV) VALUES (%s,%s,%s)'
val=[
    ('1','John','154'),
    ('2','Peter','154'),
    ('3','Amy','155'),
    ('4','Hannah','0'),
    ('5','Michael','0')
    ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,'was recorded.')
'''

'''
sql='INSERT INTO PRODUCTS (ID,NAME) VALUES(%s,%s)'
val=[
    ('154','Choclate heaven'),
    ('155','Tasty Lemons'),
    ('156','Vanila Dreams')
    ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,'was recorded.')

'''


##################INNER JOIN####################
'''
sql='select users.name AS user,products.name AS favourite from users inner join products ON users.fav=products.id'
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''

###########LEFT JOIN#####################
'''
sql='select users.name as user, products.name as favourite from users left join products on users.fav=products.id'
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''

###########RIGHT JOIN#####################
'''
sql='select users.name as user, products.name as favourite from users right join products on users.fav=products.id'
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''
