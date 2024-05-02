def one_rotation(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(0, len(arr)-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr

# arr = [1, 2, 3, 4, 5]
# res = one_rotation(arr)
# print(res)


def d_rotation(arr, d):
    n = len(arr)
    d = d % n
    temp = arr[:d]
    for i in range(d, n):
        arr[i-d] = arr[i]

    k = 0
    for j in range(n-d, n):
        arr[j] = temp[k]
        k += 1

    return arr

# [1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7]


def move_aeros(arr):

    j = -1
    for i in range(0, len(arr)):
        if arr[i] == 0:
            j = i
            break

    for k in range(j+1, len(arr)):
        if arr[k] != 0:
            temp = arr[k]
            arr[k] = arr[j]
            arr[j] = temp
            j += 1

    return arr


arr = [1, 0, 0, 2, 3, 0, 0, 4, 5, 6, 7, 8, 1]
res = move_aeros(arr)
print(res)
