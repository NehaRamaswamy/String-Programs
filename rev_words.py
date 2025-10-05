# reverse of words without built - in methods

s = 'we will get the job'
word = ''
L=[]

for ch in s:
    if ch == ' ':
        L = L + [word]
        word = ''
    else:
        word = ch + word

L = L +[word]
print(L)