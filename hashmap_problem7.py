def function(arr):
    hashmap = {}
    max_index = 0
    for index in range(0, len(arr)):
        if arr[index] in hashmap:
            hashmap[arr[index]] += 1
        else:
            hashmap[arr[index]] = 1
        max_index = max(max_index, hashmap[arr[index]])

    for i, j in hashmap.items():
        if j == max_index:
            return i


# arr = [1, 3, 2, 1, 4, 1]
arr = [10, 20, 10, 20, 30, 20, 20]
res = function(arr)
print(res)
