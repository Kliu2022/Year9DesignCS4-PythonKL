foundAt = []


def ls(list,tv):
    for i in range(0,len(list)):
        if list[i] == tv:
            print("found at: ",i)

            foundAt.append(i)


phrase = list(input("type word: "))
ls(phrase, phrase(0))
if len(phrase) > 1:
    print(foundAt)
