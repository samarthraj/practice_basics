def getSecondLargest(arr):
    max_element = 0
    second_max_element = 0
    # max number
    for i in range(1, len(arr)):  # O(N)
        if arr[i] > arr[max_element]:
            second_max_element = max_element
            max_element = i

        if arr[second_max_element] != arr[max_element] and arr[i] > arr[second_max_element]:
            second_max_element = i 
    
    return arr[second_max_element]


arr = [10, 5, 4, 6, 3, 10]
ans = getSecondLargest(arr)
print(ans)
