# Insertion Sort
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


def selection_sort(arr):
    # select the lowest element

    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[j-1]:
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
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        swap_flag = False
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap_flag = True
        if swap_flag is not True:
            break
    return arr


def binary_search(arr, target):
    low_pointer = 0
    high_pointer = len(arr) - 1

    while low_pointer <= high_pointer:
        middle = (low_pointer + high_pointer)//2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            high_pointer = middle - 1
        else:
            low_pointer = middle + 1
    return -1


arr = [2, 3, 4, 6, 7, 12, 80, 120, 900]
target = 0
res = binary_search(arr, target)
print(res)
