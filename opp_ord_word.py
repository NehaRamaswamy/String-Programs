# The opposite order of words without built - in methods

s = 'we will get the job'
word = ''
L = []

for ch in s:
    if ch == ' ':
        L = [word] + L
        word = ''
    else:
        word = word + ch
L = [word] + L
print(L)