import mysql.connector as c
con = c.connect(host = 'localhost',user='root',password='root1234',db = 'devika')
cur=con.cursor()

e = int(input('Enter Employee Number : '))
n =input('Enter Name : ')
d = input('Enter Department : ')
s = int(input('Enter Salary : '))

q = f"update employee set name = {n},dept = {d},salary={s} where empno = {e};"
cur.execute(q)
print('Data updated!')
