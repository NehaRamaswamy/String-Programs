# two-pointer method 

S='abccba'
for ind in range(0,len(S)//2):
    if S[ind] != S[-(ind+1)]:
        print('Not a Palindrome')
        break
else:
    print('Palindrome')

ind = 0
while ind >= len(S)//2:
    if S[ind] != S[-ind-1]:
        print('Not a Palindrome')
        break
    ind += 1
else:
    print('Palindrome')

