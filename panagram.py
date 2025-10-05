s = 'A quick brown fox jumps over ther lazy dog'
s1 = s.upper()

for num in range(ord('A'),ord('Z')+1):
    if chr(num) not in s1:
        print('Not Panagram')
        break
else:
    print('Panagram')