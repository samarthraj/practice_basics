def search_insert_position(arr, m):
    low = 0
    high = len(arr) - 1
    insert_index = len(arr)
    while low <= high:
        middle = (low+high)//2
        if m > arr[middle]:
            low = middle + 1
        elif m < arr[middle]:
            high = middle - 1
            insert_index = middle
    return insert_index


# arr = [1, 2, 4, 7]
# m = 6
# res = search_insert_position(arr, m)
# print(res)


def floor_or_ceil(arr, x):
    low = 0
    high = len(arr) - 1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return x, x
        if arr[mid] < x:
            low = mid + 1
            floor = arr[mid]
        elif arr[mid] > x:
            high = mid - 1
            ceil = arr[mid]
    return floor, ceil


arr = [3, 4, 7, 8, 8, 10]
x = 5
res = floor_or_ceil(arr, x)
print(res)
