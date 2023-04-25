def countingSort(array, exp):
    n = len(array)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = array[i]//exp
        count[index%10]+=10
    for i in range(1,10):
        count[i]+=count[i-1]
    i = n-1
    while i >=0:
        index=array[i]//exp
        output[count[index%10]-1]=array[i]
        count[index%10]-=1
        i-=1
    i = 0
    for i in range(len(array)):
        array[i] = output[i]
def radixSort(array):
    maxItem = max(array)
    exp = 1
    while maxItem/exp >= 1:
        countingSort(array, exp)
        exp*=10
        