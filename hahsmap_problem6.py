# Maximum distance between two occurrences of same element in array

def max_dist(arr):

    hashmap = {}
    maxDict = 0

    for index in range(0, len(arr)):
        if arr[index] not in hashmap:
            hashmap[arr[index]] = index
        else:
            a = index - hashmap[arr[index]]
            maxDict = max(maxDict, index - hashmap[arr[index]])

    return maxDict


arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
res = max_dist(arr)
print(res)
