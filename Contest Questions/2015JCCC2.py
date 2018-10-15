inputString = input('')
happy = str.count(inputString,":-)")
sad = str.count(inputString,":-(")
if happy == sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")