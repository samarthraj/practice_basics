def binary_search_insert_target(arr, m):
    n = len(arr)
    low = 0
    high = n - 1
    ans = 0

    while low <= high:
        mid = (low+high)//2

        # if m > arr[mid]:
        #     low = mid + 1
        #     #ans = mid + 1

        # elif m <= arr[mid]:
        #     high = mid - 1
        #     ans = mid

        if m <= arr[mid]:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1

    return ans


arr = [65, 63, 39, 57, 9, 29]
m = 2
res = binary_search_insert_target(arr, m)
print(res)
