def selection_sort(arr):

    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
    return arr


arr = [23, 7, 8, 0, 9, 21]
ans = selection_sort(arr)
print(ans)
# time - O(N^2)
