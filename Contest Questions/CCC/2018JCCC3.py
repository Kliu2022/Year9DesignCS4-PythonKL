inputLength = str(input(''))
a,b,c,d = inputLength.split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print(0,a,a+b,a+b+c,a+b+c+d)
print(a,0,b,b+c,b+c+d)
print(a+b,b,0,c,c+d)
print(a+b+c,b+c,c,0,d)
print(a+b+c+d,b+c+d,c+d,d,0)


