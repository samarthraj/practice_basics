# first and last occurance
def first_and_last(arr, k):
    low = 0
    high = len(arr) - 1
    first = -1
    # last = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            first = mid
            high = mid - 1
        elif arr[mid] > k:
            high = mid - 1

        elif arr[mid] < k:
            low = mid + 1

    return first, last(arr, k)


def last(arr, k):
    low = 0
    high = len(arr) - 1
    # first = -1
    last = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            last = mid
            low = mid + 1
        elif arr[mid] > k:
            high = mid - 1

        elif arr[mid] < k:
            low = mid + 1

    return last


arr = [0, 1, 1, 5]
k = 1
res = first_and_last(arr, k)
print(res)
