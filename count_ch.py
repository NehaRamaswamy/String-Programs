s = 'aaabbbbbcccndda'
res = '' 
count = 1

for ind in range(len(s)-1):
    if s[ind] == s[ind+1]:
        count += 1
    else:
        res += str(count)+s[ind]
        count = 1
res += str(count)+s[ind+1]
print(res)

res = ''
count = 1
ind = 0

while ind != len(s)-1:
    if s[ind] == s[ind + 1]:
        count += 1
    else:
        res += str(count) + s[ind]
        count = 1
    ind += 1
res += str(count) + s[ ind ]
print(res)