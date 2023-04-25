# Python3 program to sort an array of positive
# and negative numbers using bucket sort

# Function to sort arr[] of size n using
# bucket sort
def bucketSort(arr, n):
	
	# 1) Create n empty buckets
	b = []
	for i in range(n):
		b.append([])
		
	# 2) Put array elements in different
	# buckets
	for i in range(n):
		bi = int(n*arr[i])
		b[bi].append(arr[i])
	
	# 3) Sort individual buckets
	for i in range(n):
		b[i].sort()
		
	# 4) Concatenate all buckets into arr[]
	index = 0
	arr.clear()
	for i in range(n):
		for j in range(len(b[i])):
			arr.append(b[i][j])

# This function mainly splits array into two
# and then calls bucketSort() for two arrays.
def sortMixed(arr, n):
	Neg = []
	Pos = []
	
	# traverse array elements
	for i in range(n):
		if(arr[i]<0):
			# store -Ve elements by
			# converting into +ve element
			Neg.append(-1*arr[i])
		else:
			# store +ve elements
			Pos.append(arr[i])
			
	bucketSort(Neg,len(Neg))
	bucketSort(Pos,len(Pos))
	
	# First store elements of Neg[] array
	# by converting into -ve
	for i in range(len(Neg)):
		arr[i]=-1*Neg[len(Neg)-1-i]
		
	# store +ve element
	for i in range(len(Neg),n):
		arr[i]= Pos[i-len(Neg)]

# Driver program to test above function
arr = [-0.897, 0.565, 0.656, -0.1234, 0, 0.3434]
sortMixed(arr, len(arr))
print("Sorted Array is")
print(arr)

# This code is contributed by Pushpesh raj
