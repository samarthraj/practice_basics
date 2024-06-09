def remove_duplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j-1] != nums[j]:
            nums[i+1] = nums[j]
            i += 1
    return nums[:i+1]


def left_rotate(arr):
    # j = 0
    first_element = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = first_element
    return arr


def rotate_by_d(nums, k):
    # n = len(nums)
    # k = k % n

    # #brute force is this
    # first_k_elements = nums[:k+1]
    # for i in range(k+1, n):
    #     nums[i-(k+1)] = nums[i]

    # #take the first k elements and put it back
    # for j in range(0, len(first_k_elements)):
    #     nums[n-(k+1)+j] = first_k_elements[j]
    # return nums

    # optimal is till k you reverse and after k till end u reverse
    # and reverse the entire array again to get answer

    pass


# nums = [-1, -100, 3, 99]
# k = 2
# res = rotate_by_d(nums, k)
# print(res)


def move_zeros(nums):
    i = 0
    for j in range(0, len(nums)):
        if nums[j] == 0:
            i = j
            break

    for j in range(i+1, len(nums)):
        if nums[j] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
    return nums

# nums = [2, 1, 0, 3, 0, 12, 0, 8, 12, 4]
# res = move_zeros(nums)
# print(res)


def find_union(arr1, arr2):
    # brute force
    # new_set = set()

    # for i in range(0, len(arr1)):
    #     if arr1[i] not in new_set:
    #         new_set.add(arr1[i])

    # for j in range(0, len(arr2)):
    #     if arr2[i] not in new_set:
    #         new_set.add(arr2[i])

    # return new_set

    # optimal - use two pointers
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    union_arr = []
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            if arr1[i] not in union_arr:
                union_arr.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if arr2[j] not in union_arr:
                union_arr.append(arr2[j])
            j += 1

    while j < n2:
        if arr2[j] not in union_arr:
            union_arr.append(arr2[j])
        j += 1

    while i < n1:
        if arr1[i] not in union_arr:
            union_arr.append(arr1[i])
        i += 1

    return union_arr


arr1 = [1, 2, 3, 4, 5, 8, 90]
arr2 = [1, 2, 3, 6, 7, 9, 10, 12]
res = find_union(arr1, arr2)
print(res)
