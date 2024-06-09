def insertion_sort(arr):
    # You are comparing against the next one
    for index in range(1, len(arr)):
        value = arr[index]
        i = index - 1
        while i >= 0:
            if value < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = value
                i -= 1
            else:
                break
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0  # Left index
        j = 0  # Right Index
        k = 0  # merge index
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


def selection_sort(arr):
    # in this we will have to select the lowest value and then swap
    n = len(arr)

    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in range(len(arr)) if x < pivot]
    middle = [x for x in range(len(arr)) if x == pivot]
    right = [x for x in range(len(arr)) if x > pivot]

    return merge_sort(left) + middle + merge_sort(right)


def bubble_sort(arr):
    # you will swap with adjacent elemnts using a flag
    n = len(arr)
    for i in range(0, n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if swapped is not True:
            return arr
    return arr


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low+high)//2

        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            low = middle + 1
        elif target < arr[middle]:
            high = middle - 1
    return -1

# arr = [3, 5, 21, -9, -1, -20, -29]
# res = bubble_sort(arr)
# print(res)


arr = [1, 2, 3, 5, 6, 7, 20, 34, 100, 120]
target = 5
res = binary_search(arr, target)
print(res)
