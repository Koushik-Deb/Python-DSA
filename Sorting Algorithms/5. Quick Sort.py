def getPivot(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quickSort(arr, low, high):
    if low<high:
        pivot = getPivot(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

a=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
quickSort(a,0,len(a)-1)
print(*a,sep=" ")