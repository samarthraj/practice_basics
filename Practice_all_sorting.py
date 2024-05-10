# Practice all sorting techniques
# Insertion Sort
def insertion_sort(arr):
    # In insertion sort we will have to compare the values next to each other to the left
    for index in range(1, len(arr)):
        value = arr[index]
        i = index - 1  # this is for the first index 0
        while i >= 0:
            if value < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = value
                i = i - 1
            else:
                break
    return arr


def merge_sort(arr):
    # in the merge sort array we will have to break the array into two diferent arrays left and right and then sort them
    if len(arr) > 1:

        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        # we do the recursion
        merge_sort(left)
        merge_sort(right)

        # then we will do the actual merge
        i = 0  # left index
        j = 0  # right index
        k = 0  # merge index

        # compare the left most values of both left and right array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1

        # this loop is for values where in the numbers are not compared and left alone
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr


# bubble sort
def bubble_sort(arr):
    n = len(arr)
    # in the bubble sort algo we will compare the adjacent values and swap them
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
    # find the mininum index in the array and swap the values.

    n = len(arr)
    for i in range(0, n-1):
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

    # in the quick sort array we will do a sort by breaking them into left right and middle

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left_array = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right_array = [x for x in arr if x > pivot]

    return quick_sort(left_array) + middle + quick_sort(right_array)


# insertion_arr = [2, 5, 1, 0, 9, 7, -1]
# merge_array = [-2, 3, 4, 0, 8, -10, 3, -5]
# # bubble_array = [2, 5, 1, 0, 9, 7, -1, -7, 2]
# bubble_array = [1, 2, 3, 4, 5, 6, 7]
# selection_array = [-2, 3, 4, 0, 8, -10, 3, -5]
# quick_sort_array = [-2, 3, 4, 0, 8, -10, 3, -5, -100, 6]
# # res = insertion_sort(arr)
# # print(res)
# # res = merge_sort(merge_array)
# # res = bubble_sort(bubble_array)
# # res = selection_sort(selection_array)

# res = quick_sort(quick_sort_array)
# print(res)


# binary search algorithm
# if we have a sorted array and have to do some search or insertion use Binary search algorithm
def binary_search(arr, target):
    # we take a low mid and high pointers
    n = len(arr)
    low = 0
    high = n - 1
    # the low pointer should not cross over the high pointer
    while low <= high:
        mid = (low + high)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1

    return -1  # if it crosses over return -1


arr = [-18, 1, 3, 5, 6, 8, 9, 12, 23, 98]
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = binary_search(arr, 0)
print(res)
