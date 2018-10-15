a = input('')
b = input('')
c = input('')
d = input('')
e = input('')
f = input('')
wins = 0
if a == 'W':
    wins += 1
if b == 'W':
    wins += 1
if c == 'W':
    wins += 1
if d == 'W':
    wins += 1
if e == 'W':
    wins += 1
if f == 'W':
    wins += 1
if wins < 1:
    print('-1')
elif wins < 3:
    print('3')
elif wins < 5:
    print('2')
elif wins > 4:
    print('1')
