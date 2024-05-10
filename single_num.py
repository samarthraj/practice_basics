def single_num(arr):
    # hash = {}
    # j = 1
    # for i in range(0, len(arr)):  # O(N)
    #     if arr[i] not in hash:
    #         hash[arr[i]] = j
    #     else:
    #         hash[arr[i]] += j

    # for m, n in hash.items():  # O(logn)
    #     if n == 1:
    #         return m

    # total time complexity = N + N = O(2N)

    # Optimal
    ans = 0
    for i in range(0, len(arr)):
        ans = ans ^ arr[i]

    return ans


arr = [2, 2, 1]
res = single_num(arr)
print(res)
