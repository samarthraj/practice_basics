# rotate an array by k places
def rotate_by_k_places(arr, k):
    # Brute Force Methods
    # n = len(arr)
    # temp_array = arr[:k]
    # for i in range(k, n):
    #     arr[i-k] = arr[i]
    # # j = 0
    # # for i in range(n-k, n):
    # #     arr[i] = temp_array[j]
    # #     j += 1
    # # return arr

    # for i in range(n-k, n):
    #     arr[i] = temp_array[i-(n-k)]
    # return arr

    # Optimal Solution - no extra space or temp array used
    # take the elements until d and from d+1 till end and reverse them and reverse the entire array
    n = len(arr)
    k = k % n
    rotated_array = arr[k:] + arr[:k]
    return rotated_array


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
res = rotate_by_k_places(arr, k)
print(res)
