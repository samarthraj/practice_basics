def array_sum_k(arr, k):
    # Brute force
    # sum_of_subarr = 0
    # max_len = 0
    # for i in range(0,len(arr)):
    #     for j in range(i,len(arr)):
    #         sum_of_subarr += arr[j]
    #         if sum_of_subarr == k:
    #             max_len = max(max_len, len(arr[i:j+1]))
    #     sum_of_subarr = 0
    # return max_len

    j = 0
    i = 0
    sum = arr[0]
    length_longest = 0
    # sum < k, move i > k move j
    while i < len(arr):
        while j <= i and sum > k:
            sum = sum - arr[j]
            j += 1
        if sum == k:
            length_longest = max(length_longest, i-j+1)
        i += 1
        if i < len(arr):
            sum = sum + arr[i]

    return length_longest


arr = [1, 2, 3, 1, 1, 1, 1]
k = 3
res = array_sum_k(arr, k)
print(res)
