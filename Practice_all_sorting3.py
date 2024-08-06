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

# arr = [2,4,6,1,8,0,9]
# res = insertion_sort(arr)
# print(res)


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge_sort
        i = 0  # left index
        j = 0  # right index
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

# arr = [2,4,6,1,8,0,9]
# res = merge_sort(arr)
# print(res)


def selection_sort(arr):

    for i in range(0, len(arr)):
        min_value_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_value_index]:
                min_value_index = j
        if min_value_index != i:
            temp = arr[i]
            arr[i] = arr[min_value_index]
            arr[min_value_index] = temp

    return arr


# arr = [2, 4, 6, 1, 8, 0, 9]
# res = selection_sort(arr)
# print(res)


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# arr = [2, 4, 6, 1, 8, 0, 9]
# res = quick_sort(arr)
# print(res)


def bubble_sort(arr):

    for i in range(0, len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j+1] < arr[j]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swapped = True
        if swapped is not True:
            return arr
    return arr

# arr = [2, 4, 6, 10, 8, 0, 9, 1]
# res = bubble_sort(arr)
# print(res)


def binary_search(arr, target):

    low_pointer = 0
    high_pointer = len(arr) - 1

    while low_pointer <= high_pointer:
        middle = (low_pointer + high_pointer) // 2

        if target == arr[middle]:
            return middle

        elif target < arr[middle]:
            high_pointer = middle - 1

        elif target > arr[middle]:
            low_pointer = middle + 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = binary_search(arr, 5)
print(res)
