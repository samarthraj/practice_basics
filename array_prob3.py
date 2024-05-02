def remove_duplicates(arr):
    # using two pointers and the idea is to push all the duplicates to the end
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    return arr[:i+1]


arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
obj = remove_duplicates(arr)
print(obj)
