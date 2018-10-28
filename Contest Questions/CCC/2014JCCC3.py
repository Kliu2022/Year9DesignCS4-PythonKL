length = int(input(''))
rolls = []
rollsSeparatedA = []
rollsSeparatedB = []
difference = 0
scoreA = 100
scoreB = 100
for i in range(length):

    rolls.append(input(''))

for i in range(length):
    a = str(rolls[i])
    if len(a)>1:
        a,b = a.split()
    rollsSeparatedA.append(a)
    rollsSeparatedB.append(b)


for i in range(length):

    if rollsSeparatedA[i]>rollsSeparatedB[i]:

        scoreB -= int(rollsSeparatedA[i])
    elif rollsSeparatedB[i]>rollsSeparatedA[i]:
        difference = int(rollsSeparatedB[i])-int(rollsSeparatedA[i])
        scoreA -= int(rollsSeparatedB[i])

    else:
        difference = 0
print(scoreA)
print(scoreB)