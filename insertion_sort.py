def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while tmp < arr[j] and j > -1:
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr

print(insertion_sort([1,6,54,7,8]))