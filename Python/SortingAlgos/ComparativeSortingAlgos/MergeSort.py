def merge(array,leftArray,rightArray):
    i=j=k=0
    while i<len(leftArray) and j<len(rightArray):
        if leftArray[i]<=rightArray[j]:
            array[k]=leftArray[i]
            i+=1
        else:
            array[k]=rightArray[j]
            j+=1
        k+=1
    while i<len(leftArray):
        array[k]=leftArray[i]
        i+=1
        k+=1
    while j<len(rightArray):
        array[k]=rightArray[j]
        j+=1
        k+=1
def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        leftArray=array[:mid]
        rightArray=array[mid:]
        mergeSort(leftArray)
        mergeSort(rightArray)
        merge(array,leftArray,rightArray)

array = [12,11,13,5,6,7]
mergeSort(array)
print(array)
