a,b =input().split()
c,d =input().split()
t = int(input())
a = int(a)
b = int(b)
c = int(c)
d = int(d)
x = abs(a-c)
y = abs(b-d)
if x+y > t:
    print('N')
if x+y == t:
    print('Y')
if x+y < t:
    if (x+y)%2 == t%2:
        print('Y')
    else:
        print('N')

