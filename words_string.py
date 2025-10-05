# The words from a given string

s = 'we will get the job'
L = []
word = ''

for ch in s:
    if ch == ' ':
        L = L + [word]
        word = ''
    else:
        word += ch 
L = L + [word]
print(L)

word = ''
L = []
ind = 0
while ind != len(s):
    if s[ind] == ' ':
        L = L + [word]
        word = ''
    else:
        word += s[ind]
    ind += 1
L = L + [word]
print(L)

