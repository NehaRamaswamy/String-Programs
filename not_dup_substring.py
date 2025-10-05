# substring without have a duplicates

s = 'racecar'
for si in range(0,len(s)):
    for ei in range(si+1,len(s)+1):
        word = ''
        for ind in range(si,ei):
            word += s[ind]
        for ch in word:
            if word.count(ch)>1:
                break
        else:
            print(word)


s = 'racecar'
for si in range(len(s)):
    for ei in range(si+1, len(s)+1):
        word = s[si:ei]
        if len(set(word)) == len(word):   
            print(word)
