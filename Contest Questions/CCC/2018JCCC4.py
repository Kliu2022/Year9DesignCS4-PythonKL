
plants = int(input(''))
tableOld = []
plantsDecrease = 0          # Tested at end
plantsWrongOrder = 0        # Tested at end
plantsReverseOrdered = 0    # Tested at end
shouldRotate = 0            # ClockWise
tableNew = []
for i in range(plants):
    a = input('')
    tableOld.append(list(a.split(' ')))
    for k in range(plants):
        tableOld[i][k-1] = int(tableOld[i][k-1])


for i in range(plants-1):   # testing for whether or not the plants increase in size
    for k in range(plants):
        if tableOld[i][k]>tableOld[i+1][k]:
            plantsDecrease += 1

if plantsDecrease == plants*(plants-1):
    plantsDecrease = 1

for i in range(plants):
    for k in range(plants-1):
        if tableOld[i][k]<tableOld[i][k+1]:
            plantsWrongOrder += 0
        else:
            plantsWrongOrder += 1

if plantsWrongOrder == plants*(plants-1):
    plantsWrongOrder = 1
    plantsReverseOrdered = 1
elif plantsWrongOrder > 0:
    plantsWrongOrder = 1
    plantsReverseOrdered = 0
else:
    plantsWrongOrder = 0
    plantsReverseOrdered = 0
if plantsReverseOrdered == 1 and plantsDecrease == 0:
    shouldRotate = 270
if plantsWrongOrder == 0 and plantsDecrease == 0:
    shouldRotate = 0
if plantsReverseOrdered == 0 and plantsDecrease == 1:
    shouldRotate = 90
if plantsReverseOrdered == 1 and plantsDecrease == 1:
    shouldRotate = 180


if shouldRotate == 270:
    for i in range(plants):
        tableNew.append([])
        for k in range(plants):
            tableNew[i].append(tableOld[k][plants-1-i])

if shouldRotate == 90:
    for i in range(plants):
        tableNew.append([])
        for k in range(plants):
            tableNew[i].append(tableOld[plants-1-k][i])

if shouldRotate == 180:
    for i in range(plants):
        tableNew.append([])
        for k in range(plants):
            tableNew[i].append(tableOld[plants-1-i][plants-1-k])

if shouldRotate == 0:
    tableNew = tableOld

for i in range(plants):
    eachLine = str()
    for k in range(plants):
        eachLine = eachLine+str((tableNew[i][k]))+' '
    print(eachLine)
