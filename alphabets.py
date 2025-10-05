# Alphabets from a given string

S = 'he11o! eng1neer@123'
res = ' '

for ch in S:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        res += ch
print(res)

res = ' '
ind = 0
while ind != len(S):
    if 'a' <= S[ind] <= 'z' or 'A' <= S[ind] <= 'Z':
        res += S[ind]
    ind += 1
print(res)
    