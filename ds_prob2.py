def lower_bound(arr, x):
    left = 0
    right = len(arr) - 1
    lower_bound = len(arr)
    while left <= right:
        middle = (left+right)//2
        if arr[middle] >= x:
            right = middle - 1
            lower_bound = middle
        elif arr[middle] < x:
            left = middle + 1

    return lower_bound


def upper_bound(arr, x):
    left = 0
    right = len(arr) - 1
    upper_bound = len(arr)

    while left <= right:
        middle = (left+right)//2
        if arr[middle] > x:
            upper_bound = middle
            right = middle - 1
        else:
            left = middle + 1
    return upper_bound


arr = [1, 5, 5, 5, 6, 7, 7, 9, 10]
x = 5
res = upper_bound(arr, x)
print(res)

# res = lower_bound(arr, x)
# print(res)

# lower bound
# arr[middle] > x
# the first number it finds


# upper_bound
# arr[middle] > x
