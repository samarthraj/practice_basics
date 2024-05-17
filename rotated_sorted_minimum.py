import sys


def rotated_sorted_minimum(arr):
    low = 0
    high = len(arr) - 1
    lowest_target = sys.maxsize

    while low <= high:
        mid = (low+high)//2
        if arr[low] <= arr[mid]:  # checking only if the left is sorted
            # if arr[low] <= lowest_target:
            #     lowest_target = arr[low]
            lowest_target = min(lowest_target, arr[low])
            low = mid + 1
        elif arr[high] >= arr[mid]:
            # if arr[mid] <= lowest_target:
            #     lowest_target = arr[mid]
            lowest_target = min(lowest_target, arr[mid])
            high = mid - 1
    return lowest_target


arr = [3, 4, 5, 1, 2]
res = rotated_sorted_minimum(arr)
print(res)
