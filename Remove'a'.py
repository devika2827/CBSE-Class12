def rem(f,g):
    f =  open(f,'a+') 
    g = open(g,'a')
    a = f.readlines()
    for i in a:    
        if 'a' in i: 
            g.write(i)
        else:
            f.write(i)
    f.close()
    g.close()

f = input('Enter file name : ')
g = input('Enter new file name : ')
rem(f,g)