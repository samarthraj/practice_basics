# rotate an array by one to the left
def rotate_by_one(arr):
    # keep one pointer
    n = len(arr)
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr


arr = [1, 2, 3, 4, 5, 6]
res = rotate_by_one(arr)
print(res)
