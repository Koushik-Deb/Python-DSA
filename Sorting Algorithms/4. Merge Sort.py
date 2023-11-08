def merge(arr, left, right):
    i, j, k = 0, 0, 0

    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while(i<len(left)):
        arr[k] = left[i]
        k+=1
        i+=1

    while(j<len(right)):
        arr[k] = right[j]
        k+=1
        j+=1


def mergeSort(arr):
    if len(arr)>1:
        pivot = len(arr)//2
        left = arr[:pivot]
        right = arr[pivot:]
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)
        return arr
arr = [1,12,4,65,2]
mergeSort(arr)
print(arr)