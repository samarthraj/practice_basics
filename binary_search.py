# Binary Search

def binary_search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low+high)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 12, 14, 15, 20, 24, 23]
target = 20
res = binary_search(arr, target)
print(res)
