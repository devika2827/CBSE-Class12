def  isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

#a = int(input('Enter first number : '))
# = int(input('Enter last number : '))
#for i in range(a,b+1):
    if isPrime(i):
        print(i, sep = ',')

n=int(input('Enter number to be checked : '))
print(isPrime(n))
