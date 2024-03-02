import csv
def c(f):
    with open(f,'w',newline = '') as f:
        info = eval(input('Enter [User Id, Password] : '))
        cw = csv.writer(f)
        cw.writerow(info)

def r(f):
    with open(f,'r') as f:
        cr = csv.reader(f)
        for i in cr:
            print(i)

def s(f,u):
    with open(f,'r') as f:
        cr = csv.reader(f)
        for row in cr:
            if row[0] == u:
                print(f'Password : {row[1]}')
f = input('Enter file name : ')
c(f)
r(f)
u = input('Enter user id : ')
s(f,u)