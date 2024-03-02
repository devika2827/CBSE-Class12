import math
def sin(x,n):
    sin_x = 0
    for i in range(n):
        sin_x += ((x**(2*i+1))/math.factorial(2*i+1)) * ((-1)**i)
    return sin_x

x = float(input('Enter the value of x (in radians) : '))
n = int(input('Enter the no. of terms : '))
print(sin(x,n))
