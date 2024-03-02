def display(g):
    with open(g,'r') as f:
        line = f.readlines()
        for l in line:
            for w in l.split():
                print(w,end = '#')
            print()
                

g = input('Enter file name : ')
display('myfile.txt')
