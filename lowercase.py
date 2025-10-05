# Lowercase to uppercase convert
s = 'He11o! eNg1neEr@123'
res = ''

for ch in s:
    if 'A' <= ch <= 'Z':
        res += chr(ord(ch)+32)
    else:
        res +=ch
print(res)

res = ''
ind = 0
while ind != len(s):
    if 'A' <= s[ind] <= 'Z':
        res += chr(ord(s[ind])+32)
    else:
        res += s[ind]
    ind += 1
print(res)