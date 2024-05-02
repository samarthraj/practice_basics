import sys


def largest_element_in_array(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element

# arr = [2,9,0,1,3,7,20]
# res = largest_element_in_array(arr)
# print(res)

# Brute Force Solution


def second_largest_element(arr):
    arr.sort()
    i = len(arr) - 1
    second_largest = -1
    while i >= 0:
        if arr[i] != arr[i-1]:
            second_largest = arr[i-1]
            break
        else:
            i = i - 1
    return second_largest

# arr = [2,9,19,0,1,3,7,20,20]
# res = second_largest_element(arr)
# print(res)

# Optimal Solution


def second_largest_element_optimal(arr):
    # # use two pointers
    # largest_element = arr[0]
    # second_largest = -1
    # for i in range(1, len(arr)):
    #     if arr[i] > largest_element:
    #         largest_element = arr[i]
    # for j in range(0, len(arr)):
    #     if arr[j] > second_largest and second_largest < largest_element and arr[j] != largest_element:
    #         second_largest = arr[j]

    # return second_largest

    # The concept in this is as soon as one more element becomes the largest, the largest become second largest
    largest_element = arr[0]
    second_largest = -1

    smallest_element = arr[0]
    second_smallest = sys.maxsize

    for i in range(0, len(arr)):
        if arr[i] > largest_element:
            second_largest = largest_element
            largest_element = arr[i]

        if arr[i] < smallest_element:
            second_smallest = smallest_element
            smallest_element = arr[i]

    return second_largest, second_smallest, smallest_element

# arr = [2, 9, 19, 0, 1, 3, 7, 20, 20]
# res = second_largest_element_optimal(arr)
# print(res)


def check_sorted(arr):

    for i in range(0, len(arr) - 1):
        if arr[i+1] < arr[i]:
            return False
    return True


arr = [1, 2, 3, 4, 5, 0, -1, -2]
res = check_sorted(arr)
print(res)

# brute force - uses extra data structure


def remove_duplicates_from_sorted_array(arr):
    set1 = set()
    for i in range(0, len(arr)):
        if arr[i] not in set1:
            set1.add(arr[i])
    return set1


def remove_duplicates_from_sorted_array_optimal(arr):
    
    pass 


arr = [1, 4, 2, 6, 1, 1, 4, 4, 7, 7, 8]
res = remove_duplicates_from_sorted_array_optimal(arr)
print(res)
