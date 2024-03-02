import pickle
def create(f):
    i = eval(input('Enter [Roll No. , Name] : '))
    with open(f,'wb') as f:
        pickle.dump(i,f)

def g(f,r):
    with open(f,'rb') as f:
        found = False
        while not found:
            try :
                d = pickle.load(f)
                if d[0] == r:
                    print('Data exists :', d)
                    found =  True
            except:
                print('Data does not exist!')
                break
f = input('Enter file name : ')
create(f)
r = int(input('Enter roll number : '))
g(f,r)