# insertion sort

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
            elif left_arr[i] > right_arr[j]:
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

    for i in range(0, len(arr)-1):
        min_element_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_element_index]:
                min_element_index = j
        if min_element_index != i:
            temp = arr[min_element_index]
            arr[min_element_index] = arr[i]
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


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swapped = True
        if swapped is not True:
            break
    return arr


# arr = [2, 5, 1, 6, 0, -1, 9]
# res = bubble_sort(arr)
# print(res)

def binary_search_algo(arr, target):
    # we will have two pointers here left and right pointer
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left+right)//2
        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        elif target < arr[middle]:
            right = middle - 1
    return -1


# should have a sorted array
arr = [2, 3, 5, 6, 8, 9, 10, 13, 45]
res = binary_search_algo(arr, -8)
print(res)
