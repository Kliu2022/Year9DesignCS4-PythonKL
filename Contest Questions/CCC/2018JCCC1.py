digA = int(input(""))
digB = int(input(""))
digC = int(input(""))
digD = int(input(""))
telemarketer = 0
if digA == 8 or digA == 9:
    telemarketer += 1
if digB == digC:
    telemarketer += 2
if digD == 8 or digD == 9:
    telemarketer += 1
if telemarketer == 4:
    print("ignore")
else:
    print("answer")