# Add the digits available in string

s = 'He11o! eNg1nEer@123'
res = 0
for ch in s:
    if '0' <= ch <= '9':
        res += int(ch)
print(res)

res = 0
ind = 0
while ind != len(s):
    if '0' <= s[ind] <= '9':
        res += int(s[ind])
    ind += 1
print(res)