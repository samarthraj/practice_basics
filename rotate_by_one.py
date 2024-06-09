def rotate_by_one(arr):

    n = len(arr)
    j = 0
    first_element = arr[j]
    for i in range(1, n):
        arr[i-1] = arr[i]

    arr[n-1] = first_element
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
res = rotate_by_one(arr)
print(res)
