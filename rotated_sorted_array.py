def search_rotated_sorted(arr, target):
    low = 0
    high = len(arr) - 1 

    while low <= high: 
        mid = (low+high)//2
        if arr[mid] == target: 
            return mid 
        elif arr[low] <= arr[mid]: #means if the left is sorted according to mid 
            if arr[low] <= target and target <= arr[mid]: 
                high = mid - 1
            else:
                low = mid + 1

        elif arr[high] > arr[mid]: #means if the right is sorted according to mid 
            if arr[high] >= target and target >= arr[mid]: 
                low = mid + 1
            else:
                high = mid - 1
    return -1 

arr = [4, 5, 6, 7, 0, 1, 2]
target = 12
res = search_rotated_sorted(arr, target)
print(res)
