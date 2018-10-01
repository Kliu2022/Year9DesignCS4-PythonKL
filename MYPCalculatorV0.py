#By Kevin Yunqiao Liu, Sep 30, 2018
#MYP Calculator V0

sum = 0

a=0
b=0
c=0
d=0
totalSum=0

def mypAverage (int1,int2,int3,int4): 
	
	sum = int1+int2+int3+int4

	mypLookup = [10,20,30,40,50,52,54,57,60,62,64,66,68,71,74,77,80,83,84,86,88,90,92,93,94,95,96,97,98,98,99,100]

	return mypLookup[sum-1]

for i in range(8):

	a = input("Input your Criterion A Mark (out of 8) for subject number "+str((i+1)))
	b = input("Input your Criterion A Mark (out of 8) for subject number "+str((i+1)))
	c = input("Input your Criterion A Mark (out of 8) for subject number "+str((i+1)))
	d = input("Input your Criterion A Mark (out of 8) for subject number "+str((i+1)))
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)


	totalSum += mypAverage(a,b,c,d)

finalAverage = totalSum/8

print("Your average is: " + str(finalAverage))
