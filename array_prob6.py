# move all zeros to the end
def move_all_zeros(arr):
    j = -1
    for i in range(0,len(arr)):
        if arr[i] == 0: 
            j = i 
            break 
    
    for k in range(j+1,len(arr)): 
        if arr[k] != 0:
            temp = arr[k]
            arr[k] = arr[j] 
            arr[j] = temp 
            j += 1

    return arr

arr = [1, 0, 2, 0, 0, 3, 4]
res = move_all_zeros(arr)
print(res)
