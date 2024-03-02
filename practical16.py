stk = []
def puch(d):
    for i,j in d.items():
        if j>75:
            stk.append(i)
def pop():
    if len(stk)==0:
        print('Stack is')
        return
    stk.pop()
    for i in stk[::-1]:
        print(i)
def display():
    for i in stk[::-1]:
        print(i)
def menu():
    while True:
        print('1. Push\n2. Pop and Display\n3. Display all contents\n4. Exit')
        ch = int(input('Enter your choice : '))
        if ch == 1:
            d = eval(input('Enter data {name : marks} : '))
            puch(d)
        elif ch ==2:
            pop()
        elif ch==3:
            display()
        elif ch==4:
            break
        else:
            print('Invalid Choice!')

menu()