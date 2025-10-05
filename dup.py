#remove duplicates in the string
S = 'engineering'
res = ''
for ch in S:
    if ch not in res:
        res += ch
print(res)

ind = 0
while ind != len(S):
    if S[ind] not in res:
        res += S[ind]
    ind += 1
print(res)