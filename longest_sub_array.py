def array_sum_k(arr, k):
    # Brute Force
    # sum = 0
    # max_length = 0
    # for i in range(0, len(arr)):
    #     for j in range(i, len(arr)):
    #         sum += arr[j]
    #         if sum == k and len(arr[i:j+1]) > max_length:
    #             max_length = len(arr[i:j+1])
    #     sum = 0
    # return max_length

    # Hashing using better solution

    hash = {}
    


arr = [1, 2, 3, 1, 1, 1, 1]
k = 3
res = array_sum_k(arr, k)
print(res)
