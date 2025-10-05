# Substring from a given string 

s = 'racecar'

for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        print(s[si:ei])

# Substring from a given string without slicing
L = []
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word = ''
        for ind in range(si,ei):
            word += s[ind]
        L.append(word)
print(L)

#using while loop
L = []
si = 0
while si != len(s):
    ei = si + 1
    while ei != len(s)+1:
        word = ''
        ind = si
        while ind != ei:
            word += s[ind]
            ind += 1
        L.append(word)
        ei += 1
    si += 1
print(L)
