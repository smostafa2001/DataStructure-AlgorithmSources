def bubbleSort(array):
    n = len(array)-1
    for i in range(0,n):
        flag = False
        for j in range(0, n):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
                flag = True
        if not flag: break
array = [20,10,12,7]
bubbleSort(array)
print(array)