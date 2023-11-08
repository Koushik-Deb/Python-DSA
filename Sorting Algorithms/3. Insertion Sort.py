def insertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
                arr[j+1] = arr[j]
                j-=1
        arr[j+1] = temp

    return arr


print(insertionSort([1,12,4,65,2]))
