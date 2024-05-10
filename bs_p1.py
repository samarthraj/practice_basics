
def binary_search(n, arr, target):

    low = 0
    high = n-1
    ans = n

    while low <= high:
        mid = (low+high)//2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        elif arr[mid] <= target:
            low = mid + 1

    return ans


arr = [1, 4, 7, 8, 10]
target = 7
n = 5
res = binary_search(n, arr, target)
print(res)
