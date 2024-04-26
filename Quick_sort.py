# In this quick sort we shall take the middle element as the pivot and do our logic

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [2, 5, 0, 9, 1, -9, 3, 4]
res = quick_sort(arr)
print(res)
