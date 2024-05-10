def second_largest_element(arr):

    # optimal
    max_ele = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max_ele:
            second_max = max_ele
            max_ele = arr[i]
        second_max = arr[i]
    return [max_ele, second_max]


# arr = [1, 3, 6, 2, 7, 89, 12]
# res = second_largest_element(arr)
# print(res)

def remove_duplicates(arr):
    j = 0
    for i in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[j+1] = arr[i]
            j += 1
    return arr[:j+1]


arr = [1, 1, 3, 3, 5, 6, 8, 8, 12, 13, 15, 15]

# res = remove_duplicates(arr)
# print(res)
# print(set(arr))


def left_rotate_array_by_one(arr):
    temp = arr[0]
    for i in range(1, len(arr)):  # O(N)
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr


def left_rotate_by_d_spaces(arr, d):
    # Brute Force Solution
    # n = len(arr)
    # d = d % n #2
    # temp = arr[:d]
    # for i in range(d,len(arr)):
    #     arr[i-d] = arr[i]

    # for j in range(0, len(temp)):
    #     arr[n - d] = temp[j]
    #     d -= 1

    # return arr

    # Optimal Approach

    n = len(arr)
    d = d % n  # 2

    arr[:d].reverse()

    # arr2 = arr[d:].reverse()
    # arr.reverse()

    print(arr)


arr = [1, 2, 3, 4, 5]
d = 7
# res = left_rotate_array_by_one(arr)
# res = left_rotate_by_d_spaces(arr, d)
# print(res)


def move_zeros_to_end(arr):
    j = -1
    for i in range(0, len(arr)):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1, len(arr)):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1

    return arr


arr = [1, 3, 4, 0, 0, 5, 7, 0, 9, 1, 0, 12]
# res = move_zeros_to_end(arr)
# print(res)


def remove_duplicates(arr):

    j = 0
    for i in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[j+1] = arr[i]
            j += 1
    return arr[:j+1]


arr = [1, 2, 3, 4, 4, 4, 5, 5]
# res = remove_duplicates(arr)
# print(res)


def move_zeros(arr):
    j = 0
    for i in range(0, len(arr)):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1, len(arr)):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    return arr


arr = [1, 3, 4, 0, 0, 5, 7, 0, 9, 1, 0, 12]
res = move_zeros(arr)
print(res)
