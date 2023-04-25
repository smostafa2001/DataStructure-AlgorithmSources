def partition(array,l,u):
    pivot = array[l]
    j=l
    for i in range(l+1,u+1):
        if array[i]<pivot:
            j+=1
            array[i],array[j]=array[j],array[i]
    array[j],array[l]=array[l],array[j]
    return j

def quick(array,l,u):
    if(l<u):
        j=partition(array,l,u)
        quick(array,l,j-1)
        quick(array,j+1,u)
array=[30,20,40,15,17,50,12,45,10]
quick(array,0,len(array)-1)
print(array)