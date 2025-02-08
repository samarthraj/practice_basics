def selection_sort(arr):
    # Here you select the least number and put it in its position
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr


def bubble_sort(arr):
    # here we swap adjacent elements
    for i in range(0, len(arr)):
        swapped = False
        # at the end of this one run the last element will be in its place
        for j in range(0, len(arr)-1-i):
            if arr[j+1] < arr[j]:  # only inner loop j coz its a swap
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swapped = True

        if swapped != True:
            break

    return arr


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # coz you will want to have a single number to merge and until then recursion happens
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


arr = [9, 10, -2, 0, -23, 30, -400]
# ans = selection_sort(arr)
# ans = bubble_sort(arr)
ans = merge_sort(arr)
print("merge sort" + str(ans))
