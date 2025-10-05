# Substrings which are palindrome
s = 'racecar'

for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word = ''
        for ind in range(si,ei):
            word = s[si:ei]
        if word == word[::-1]:
            print(word)
print()
# Without using slicing method
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word = ''
        for ind in range(si,ei):
            word += s[ind]
        rev = ''
        for ch in word:
            rev = ch + rev
        if word == rev:
            print(word)