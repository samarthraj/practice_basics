def single_element_sorted(arr):
    low = 0
    high = len(arr) - 1
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    while low <= high:
        mid = (low+high)//2
        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        else:
            if arr[mid] == arr[mid - 1] and (mid % 2 == 0) or arr[mid] == arr[mid+1] and (mid % 2) != 0:
                high = mid - 1
            else:
                low = mid + 1


arr = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 8, 8]
res = single_element_sorted(arr)
print(res)
