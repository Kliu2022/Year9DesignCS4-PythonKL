import math
D = int(input(''))
hour = 0
a = 0
b = 0
c = 0
d = 0
k = 0
minute = 0
solutions = 0
if D > 720:
    k = math.floor(D/720)
    D = D - k*720
    solutions += 31*k
for i in range(D):
    hour = math.floor(i / 60)
    minute = int(i - (60 * hour)+1)
    if hour > 12:
        hour = hour % 12
    if hour == 0:
        hour = 12
    if hour > 9:
        a = 1
        b = hour - 10
    if hour < 10:
        a = 0
        b = hour
    if minute < 10:
        c = 0
        d = minute
    if minute > 9:
        tens = math.floor(minute / 10)
        c = tens
        d = minute - (10 * tens)
    d1 = d - c
    d2 = c - b

    if a == 0:

        if d1 == d2:
            solutions += 1

        else:
            solutions += 0
    if a > 0:
        d1 = d-c
        d2 = c-b
        d3 = b-a
        if d1 == d2 == d3:
            solutions += 1

        else:
            solutions += 0
    minute += 1
print(solutions)