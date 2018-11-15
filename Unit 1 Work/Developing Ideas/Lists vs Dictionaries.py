questionList = [
"Question 1: What is 1+2", 
"Question 2: What is 4-2", 
"Question 3: What is 2-3"
]

for i in questionList:
	print(i)


switcher = {
	0: "Question 1: What is 2+2",
	1: "Question 2: What is 2+4",
	2: "Question 3: What is 2+5",
}

for j in range(7):
	print(switcher.get(j))
