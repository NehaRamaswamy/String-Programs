# Check the given strings are anagrams or not
# listen - slient, earth - heart, evil - vile, night - thing , admirer   - married
s1 = 'listen'
s2 = 'slient'

if len(s1) == len(s2):
    for ch in s1:
        if (ch not in s2) or (s1.count(ch) != s2.count(ch)):
            print('Not an Anagram')
            break
    else:
        print('An Anagram')
else:
    print('Not an Anagram')