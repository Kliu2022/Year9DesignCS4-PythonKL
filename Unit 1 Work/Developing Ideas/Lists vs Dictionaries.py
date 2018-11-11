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
	3: "Question 4: What is 2+67",
	4: "Question 5: What is 2+7",
	5: "Question 6: What is 2+8",
	6: "Question 7: What is 2+9",
	7: "Question 8: What is 2+20",

}

for j in range(7):
	print(switcher.get(j))
