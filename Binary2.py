import pickle
def create(f):
    with open(f,'ab') as f:
        i = eval(input('Enter [Roll No, Name, Marks] : '))
        pickle.dump(i,f)

def update(f,r):
    with open(f,'rb+')as f:
        try:
            while True:
                pos = f.tell()
                d = pickle.load(f)
                if d[0]==r:
                    nm = int(input('Enter new marks : '))
                    d[2] = nm
                    f.seek(pos)
                    pickle.dump(d,f)
                    print('Data updated!')
        except:
            pass

f = input('Enter file name : ')
create(f)
r = int(input('Enter roll number : '))
update(f,r)