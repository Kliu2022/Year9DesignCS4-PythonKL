a1,a2,a3,a4 = input('').split(' ')
b1,b2,b3,b4 = input('').split(' ')
c1,c2,c3,c4 = input('').split(' ')
d1,d2,d3,d4 = input('').split(' ')
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
a4 = int(a4)
b1 = int(b1)
b2 = int(b2)
b3 = int(b3)
b4 = int(b4)
c1 = int(c1)
c2 = int(c2)
c3 = int(c3)
c4 = int(c4)
d1 = int(d1)
d2 = int(d2)
d3 = int(d3)
d4 = int(d4)
a = a1+a2+a3+a4
b = b1+b2+b3+b4
c = c1+c2+c3+c4
d = d1+d2+d3+d4
e = a1+b1+c1+d1
f = a2+b2+c2+d2
g = a3+b3+c3+d3
h = a4+b4+c4+d4
if a == b == c == d == e == f == g == h:
    print("magic")
else:
    print("not magic")