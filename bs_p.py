# Binary Search
def binary_search(arr, target):
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


arr = [2, 3, 4, 5, 6, 7, 8, 10, 12, 32]
target = 7
res = binary_search(arr, target)
# print(res)


def selection_sort(arr):

    # find the minimum index element and swap
    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp

    return arr


arr = [1, 4, 1, 6, -1, 7, 1, 8, 9, 10]
res = selection_sort(arr)
# print(res)


def insertion_sort(arr):

    # check if the next number is lesser then the current number
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


arr = [1, 4, 1, 6, -1, 7, 1, 8, 9, 10]
res = insertion_sort(arr)
print(res)
