length = int(input(""))
a = 0
b = 0
votes = input("")
for i in range(len(votes)):
    if votes[i] == 'A':
        a += 1
b = length - a
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")