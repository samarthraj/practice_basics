# binary search
# In binary search algo we will have a low high and a mid pointer and check with the pointer

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
        elif target > arr[mid]:
            low = mid + 1

    return -1  # if target not present


arr = [1, 2, 3, 4, 5, 6, 7, 9, 12]
res = binary_search(arr, -9)
print(res)
