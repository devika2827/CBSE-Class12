def count_vowel(f):
    with open(f,'r') as f:
        data = f.read()
    vowels = {'a' : 0, 'e':0,'i':0,'o':0,'u': 0}
    for char in data:
        if char in vowels:
            vowels[char] += 1

    return vowels

f = input('Enter file name : ')
print(count_vowel(f))