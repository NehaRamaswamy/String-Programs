s = 'He11o! eNg1neEr@123'
res = ''

for ch in s:
    if 'a' <= ch <= 'z':
        res += chr(ord(ch)-32)
    else:
        res += ch
print(res)

res = ''
ind = 0
while ind != len(s):
    if 'a' <= s[ind] <= 'z':
        res += chr(ord(s[ind])-32)
    else:
        res += s[ind]
    ind += 1
print(res)