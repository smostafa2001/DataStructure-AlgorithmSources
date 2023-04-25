def insertionSort(array):
    for i in range(1,len(array)):
        y = array[i]
        j = i-1
        while y<array[j] and j>=0:
            array[j+1]=array[j]
            j=j-1
        array[j+1] = y
array = [20,10,30,25,7]
insertionSort(array)
print(array)