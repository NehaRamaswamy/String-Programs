# Reverse of the word in opposite order

s = 'we will get the job'
word = ''
L = []

for ch in s:
    if ch == ' ':
        L = [word] + L
        word = ''
    else:
        word = ch + word
L = [word] + L
print(L)