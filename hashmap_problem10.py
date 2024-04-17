# Given two arrays, arr1 and arr2 of equal length N, the task is to find if the given arrays are equal or not.

def function(a, b):
    hashmap_a1 = {}
    hashmap_a2 = {}

    for i in range(0, len(a)):
        if a[i] in hashmap_a1:
            hashmap_a1[a[i]] += 1
        else:
            hashmap_a1[a[i]] = 1

    for j in range(0, len(b)):
        if b[j] in hashmap_a2:
            hashmap_a2[b[j]] += 1
        else:
            hashmap_a2[b[j]] = 1

    print(hashmap_a1, hashmap_a2)
    for key, value in hashmap_a1.items():
        if key not in hashmap_a2.keys():
            return ('No')
        elif hashmap_a1[key] != hashmap_a2[key]:
            return ('No')
    return ('Yes')

# a = [1, 5, 3, 8]
# b = [5, 4, 6, 7]

# a = [1, 2, 5, 4, 0, 2, 1]
# b = [2, 4, 5, 0, 1, 1, 2]


a = [1, 7, 1]
b = [7, 7, 1]

res = function(a, b)
print(res)
