def pal(str):
    return str == str[::-1]
    
    

str = input('Enter the string : ')
if pal(str):
    print('This is a Palindrome')
else:
    print('This is not a Palindrome')
