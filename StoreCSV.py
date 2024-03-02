import csv
def c(f):
    with open(f,'a') as f:
        cw = csv.writer(f)
        add = True
        while add:
            info = eval(input('Enter [empno,name, salary] : '))
            cw.writerow(info)
            add = 'y' == input('Add more data [y/n] : ')

def s(f,e):
    with open(f,'r') as f:
        r = csv.reader(f)
        for row in r:
            if str(row[0])==str(e):
                print(row[1],row[2])
                break
        else:
            print('Data does not exist')

f = input('Enter file name : ')
c(f) 
e = input('Enter the employee number : ')          
s(f,e)