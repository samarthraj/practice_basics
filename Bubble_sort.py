# Bubble Sort Algorithm
# In the bubble sort algorithm we push the max by adjacent swaps to the last
# Selection Sort
# In Selection sort what we do is choose a max or min element from the list and compare each element with it and then swap
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if swapped is False:
            break
    return arr


arr = [2, 5, 7, 1, 8, 0]
# arr = [1,2,3,4,5]
res = bubble_sort(arr)
print(res)
