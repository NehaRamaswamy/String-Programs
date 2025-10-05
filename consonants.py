# Consonants from a given string
S = 'he11o! eng1neer@123p'
res = ''

for ch in S:
    if ch not in 'AEIOUaeiou' and 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        res += ch
print(res)

res = ''
ind = 0
while ind != len(S):
    if S[ind] not in 'AEIOUaeiou' and 'a' <= S[ind] <= 'z' or 'A' <= S[ind] <= 'Z':
        res += S[ind]
    ind += 1
print(res)

