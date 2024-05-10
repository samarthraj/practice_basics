# largest element
import sys


def largest_element(arr):
    # Brute force will be to just sort the array and then find the last element
    # optimal approach will be to use pointers
    max_ele = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]
    return max_ele

# arr = [1, 4, 6, 1, 9, 10, 12, 0]
# res = largest_element(arr)
# print(res)


def second_largest_smallest_element(arr):
    # Brute force - O(2N) Space = O(N)
    # first_largest = arr[0]
    # second_largest = -1

    # first_smallest = arr[0]
    # second_smallest = sys.maxsize
    # for i in range(0, len(arr)):
    #     if arr[i] > first_largest:
    #         first_largest = arr[i]

    # for j in range(0, len(arr)):
    #     if arr[j] < first_largest and arr[j] > second_largest and arr[j] != first_largest:
    #         second_largest = arr[j]
    # # return [first_largest, second_largest]
    # for k in range(0, len(arr)):
    #     if arr[k] < first_smallest:
    #         first_smallest = arr[k]

    # for m in range(0, len(arr)):
    #     if arr[m] > first_smallest and arr[m] < second_smallest and arr[m] != second_smallest:
    #         second_smallest = arr[m]

    # return [first_largest, second_largest, first_smallest, second_smallest]

    # Optimal Approach is that when ever the first element is is changed it automatically becomes 2nd
    max_ele = arr[0]
    second_max = -1
    for i in range(0, len(arr)):
        if arr[i] > max_ele:
            second_max = max_ele
            max_ele = arr[i]
        elif arr[i] > second_max:
            second_max = arr[i]
    return [max_ele, second_max]


# arr = [1, 4, 6, 1, 9, 100, 12, 0]
# res = second_largest_smallest_element(arr)
# print(res)


def remove_duplicates(arr):
    # brute force will be to use sets but its using another ds and taking up space
    # use optimal approach is to use pointers in an array which is sorted.
    # i = 0
    # for j in range(1,len(arr)):
    #     if arr[i] != arr[j]:
    #         arr[i+1] = arr[j]
    #         i += 1
    # return arr
    pass


arr = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9, 10]
res = remove_duplicates(arr)
print(res)
