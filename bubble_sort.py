def bubble_sort(arr):

    for i in range(0, len(arr)):
        swapped = False
        for j in range(0, len(arr)-1-i):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if swapped == False:
            break

    return arr


arr = [30, 80, 9, -1, 3, 45, 0, 8]
arr = [0, 1, 2, 3]
ans = bubble_sort(arr)
print(ans)
