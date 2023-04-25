def selectionSort(array):
    for i in range(len(array)-1,0,-1):
        max = array[0]
        index = 0
        for j in range(1,i+1):
            if(array[j]>max):
                max = array[j]
                index = j
        array[index] = array[i]
        array[i]=max
array = [10,20,15,5,12]
selectionSort(array)
print(array)