b = []
def push(b):
    t = input("Enter the book's title : ")
    b.append(t)
def pop(b):
    if len(b) == 0:
        print('Stack is empty')
    else:
        return b.pop()
def display(b):
    for i in b[::-1]:
        print(i)
def menu():
    while True:
        print('1. Push\n2. Pop\n3. Display\n4. Exit')
        ch = int(input('Enter your choice : '))
        if ch == 1:
            push(b)
        elif ch ==2:
            pop(b)
        elif ch==3:
            display(b)
        elif ch==4:
            break
        else:
            print('Invalid Choice!')

menu()