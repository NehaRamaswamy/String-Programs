s = 'he11o! eng1neer@123'
res = ''

for ch in s:
    if '0' <= ch <= '9':
        res += ch

print(res)

res = ''
ind  = 0
while ind != len(s):
    if '0' <= s[ind] <= '9':
        res += s[ind]
    ind += 1
print(res)