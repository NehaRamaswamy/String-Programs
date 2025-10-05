# Count the occurance of character in string

S = 'engineering'
res = ''

for ch in S:
    if ch not in res:
        res += ch
for ch1 in res:
    print(f'{ch1} = {S.count(ch1)}')

print()

ind = 0
while ind != len(S):
    if S[ind] not in res:
        res += S[ind]
    ind += 1

for ch1 in res:
    print(f'{ch1} = {S.count(ch1)}')
