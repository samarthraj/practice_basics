# Selection Sort
# In Selection sort what we do is choose a max or min element from the list and compare each element with it and then swap

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):  # because the last element would be sorted by the end of the iteration
        min_index = i
        for j in range(i+1, n):  # goes all the way till the end of the list
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr


arr = [2, 5, 7, 1, 8, 0]
res = selection_sort(arr)
print(res)
