def menu():
    while True:
        print('1. Add rec\n2. Search rec')
        ch = int(input('Enter choice'))
        if ch == 1:
            addrec()
        if ch ==2 :
            R = (input('Enter roll no'))
            searchrec(R)
import csv

def  addrec():
    with open('std.csv','a',newline = '') as f:
        roll = (input('Enter roll'))
        name = input('Enter name')
        marks = (input('enter marks'))
        cw= csv.writer(f)
        d = [roll,name,marks]
        cw.writerow(d)

def searchrec(R) :
    d = []
    with open('std.csv') as f:
        cr =csv.reader(f)
        for i in cr:
            d.append(i)
        for i in d:
            if i[0] == R:
                i[1] = input('enter coreect name')
                i[2] = ((input('Enter correct marks')))
                
    with open('std.csv','w',newline='') as f:
        wr = csv.writer(f)
        wr.writerows(d)
menu()