number = int(input(''))
yesterday = list(input(''))
today = list(input(''))
output = 0
for i in range(number):
    if yesterday[i] == 'C' and today[i] == 'C':
        output += 1
    else:
        output += 0

print(output)