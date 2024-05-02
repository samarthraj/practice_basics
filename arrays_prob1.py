def getSecondOrderElements(arr):
    # Write your code here.
    largest_element = arr[0]
    second_largest = -1

    for i in range(0, len(arr)):
        if arr[i] > largest_element:
            largest_element = arr[i]
    for j in range(0, len(arr)):
        if arr[j] > second_largest and second_largest < largest_element and arr[j] != largest_element:
            second_largest = arr[j]

    return largest_element, second_largest


arr = [2, 6, 1, 4, 9, 0]
obj = getSecondOrderElements(arr)
print(obj)
