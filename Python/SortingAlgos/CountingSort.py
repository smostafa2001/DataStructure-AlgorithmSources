def countingSort(inputArray):
    maxElement = max(inputArray)
    minElement = min (inputArray)
    rangeOfElements = maxElement - minElement +1
    count = [0 for i in range(rangeOfElements)]
    outputArray = [0 for i in range(len(inputArray))]

    for i in range(0,len(inputArray)):
        count[inputArray[i]-minElement]+=1
    

    for i in range(1,len(count)):
        count [i] += count[i-1]
    

    for i in range(len(inputArray)-1, -1,-1):
        outputArray [count[inputArray[i]-minElement]-1] = inputArray[i]
        count[inputArray[i] - minElement] -= 1
    

    return outputArray



arr = [-5,-10,0,-3,8,5,-1,10]
ans = countingSort(arr)
print(str(ans))
