def countingSort(arr):
    maxValue = max(arr)
    aux = [0]*(maxValue+1)
    result = [0]*len(arr)

    for val in arr:
        aux[val]+=1
    
    for i in range(1, maxValue+1):
        aux[i]+=aux[i-1]

    for val in arr[::-1]:
        aux[val]-=1
        result[aux[val]] = val
    return result

a=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print(countingSort(a))