# Vowels in string
S='engineering'
res = ' '

for ch in S:
    if ch in 'AEIOUaeiou':
        res += ch
print(res)

res = ' '
ind = 0
while ind != len(S)-1:
    if S[ind] in 'AEIOUaeiou':
        res += S[ind]
    ind += 1
print(res)


# Vowels without duplicates
res = ' '

for ch in S:
    if ch in 'AEIOUaeiou' and ch not in res:
        res += ch
print(res)


res = ' '

ind = 0
while ind != len(S):
    if S[ind] in 'AEIOUaeiou' and S[ind] not in res:
        res += S[ind]
    ind += 1
print(res)