def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j]<=arr[minIndex]:
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex], arr[i]

    return arr


print(selectionSort([1,12,4,65,2]))
