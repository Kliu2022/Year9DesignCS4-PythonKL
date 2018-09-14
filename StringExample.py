name = input("What is your name: ")

letters1 = name[0:2] #inclusive:exclusive

print(letters1)

length = len(name)

print(length)

for i in range(length):
	print(name[i])