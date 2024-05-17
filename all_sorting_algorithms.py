def insertion_sort(arr):

    for index in range(1, len(arr)):
        value = arr[index]
        i = index - 1

        while i >= 0:
            if value < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = value
                i = i - 1
            else:
                break
    return arr


def merge_sort(arr):

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


def bubble_sort(arr):
    # we use flag
    n = len(arr)
    for i in range(0, n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j+1] < arr[j]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swapped = True
        if swapped is not True:
            break

    return arr


def selection_sort(arr):
    # select the minimum element and swap
    n = len(arr)

    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp

    return arr


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [2, 9, -20, 10, 3, -21]
res = quick_sort(arr)
# print(res)


# binary search algorithm, has to be sorted array
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high)//2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
    return -1


arr = [1, 2, 2, 4, 6, 8, 9, 12, 32]
target = 2
res = binary_search(arr, target)
print(res)
