# Substring in opposite order 
s = 'racecar'
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word = ''
        for ind in range(si,ei):
            word = s[si:ei]
        print(word[::-1])

si = 0
while si != len(s):
    ei = si + 1
    while ei != len(s)+1:
        word = ''
        ind =si
        while ind != ei:
            word = s[si:ei]
            ind += 1
        print(word[::-1])
        ei += 1
    si += 1
    