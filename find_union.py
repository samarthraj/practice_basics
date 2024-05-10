# find union in arrays
def find_union(arr1, arr2):
    # Brute Force
    new_set = set()
    for i in range(0, len(arr1)):
        if arr1[i] not in new_set:
            new_set.add(arr1[i])

    for i in range(0, len(arr2)):
        if arr2[i] not in new_set:
            new_set.add(arr2[i])
    return new_set

    # # Optimal
    # union_array = []
    # i = 0
    # j = 0 

    # while i < len(arr1) and j < len(arr2):
    #     if arr1[i] <= arr2[j] and arr1[i] not in union_array: 
    #         union_array.append(arr1[i]) 
    #         i += 1

    #     if arr1[i] > arr2[j] and arr1[j] not in union_array:  
    #         union_array.append(arr2[j])
    #         j += 1
    
    return union_array

arr1 = [1, 2, 3, 4, 6]
arr2 = [2, 3, 5]
res = find_union(arr1, arr2)
print(res)
