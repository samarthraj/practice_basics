def longest_sum(arr, m):
    #brute force 
    # longest_length = 0
    # for i in range(0, len(arr)): 
    #     sum = 0
    #     for j in range(i, len(arr)): 
    #         sum += arr[j] 
    #         if sum == m:
    #             longest_length = max(longest_length, len(arr[i:j+1]))
    # return longest_length

    #optimize with two pointer 
    i = 0
    j = 0 
    sum = 0
    while i < len(arr) and j < len(arr): 
        sum = arr[i:j]  


arr = [10, 5, 2, 7, 1, 9]
m = 15
res = longest_sum(arr, m)
print(res)
