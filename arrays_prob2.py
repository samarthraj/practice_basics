import sys


def getSecondOrderElements(a):
    largest_element = a[0]
    second_largest = -1

    smallest_element = a[0]
    second_smallest = sys.maxsize

    for i in range(1, len(a)):
        if a[i] > second_largest:
            second_largest = a[i]
        if a[i] > largest_element:
            second_largest = largest_element
            largest_element = a[i]

        if a[i] < second_smallest:
            second_smallest = a[i]
        if a[i] < smallest_element:
            second_smallest = smallest_element
            smallest_element = a[i]

    return second_largest, second_smallest


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
obj = getSecondOrderElements(arr)
print(obj)
