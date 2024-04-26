# Insertion sort
def insertion_sort(arr):
    # in this insertion sort what we do is we compare the next values with all the left values
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
    # In merge sort we devide the array into two left and right and then compare and merge
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        # [-2,3,5] [-1,9,1]
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


def selection_sort(arr):
    # In selection sort we choose the maximum element and then push it to the last
    n = len(arr)
    # we choose n-1 because the last one will be already sorted by the time we reach there
    for i in range(0, n - 1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp

    return arr


def bubble_sort(arr):
    # in bubble sort we will have to compare adjacent values and then swap them if found less
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


arr = [2, 4, 1, 0, 9, 401, -2, -99]
# insertion_res = insertion_sort(arr)
# merge_res = merge_sort(arr)
# selection_res = selection_sort(arr)

bubble_res = bubble_sort(arr)
print(bubble_res)
