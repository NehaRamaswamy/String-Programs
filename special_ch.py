s = 'he11o! eng1neer@123'
res = ''

for ch in s:
    if not(('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')):
        res += ch
print(res)

res = ''
ind = 0
while ind != len(s):
    if not(('a' <= s[ind] <= 'z') or ('A' <= s[ind] <= 'Z') or ('0' <= s[ind] <= '9')):
        res += s[ind]
    ind += 1
print(res)