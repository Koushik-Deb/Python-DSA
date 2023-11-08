def getPivot(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quickSelect(arr, low, high, k):
    if low<high:
        pivot = getPivot(arr, low, high)
        
        if pivot == k:
            return arr[:k]
        elif pivot>k:
            return quickSelect(arr, low, pivot-1, k)
        else:
            return quickSelect(arr, pivot+1, high, k)

a=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print(quickSelect(a,0,len(a)-1, 5))
