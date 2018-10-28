a = int(input(""))
b = int(input(""))
c = int(input(""))
d = a+b+c
e = 180


if d == e:
    if a == 60 and b == 60 and c == 60:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")