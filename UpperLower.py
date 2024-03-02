def count(f):
    c = {'lower': 0,'upper':0,'vowel':0,'consonant':0}
    with open(f,'r') as f:
        data = f.read()
    for char in data:
        if char.isupper() :
            c['upper'] += 1
        elif char.islower():
            c['lower'] +=1
        if char in 'aeiou':
            c['vowel'] +=1
        elif not char.isdigit():
            c['consonant'] += 1
    return(c)       
f = input('Enter file name : ')
print(count(f))         