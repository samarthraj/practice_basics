def isSubset(a1, a2, n, m):

    new_hash_a1 = {}
    new_hash_a2 = {}

    for val in range(0, len(a1)):
        if a1[val] in new_hash_a1:
            new_hash_a1[a1[val]] += 1
        else:
            new_hash_a1[a1[val]] = 1

    for val in range(0, len(a2)):
        if a2[val] in new_hash_a2:
            new_hash_a2[a2[val]] += 1
        else:
            new_hash_a2[a2[val]] = 1

    print(new_hash_a1, new_hash_a2)

    # for key1,value1 in new_hash_a1.items():
    #     for key2,value2 in new_hash_a2.items():
    #         if key2 not in new_hash_a1.keys():
    #             return ('No')
    #         elif key2 == key1 and value2 > value1:
    #             return ('No')
    # return ('Yes')

    for key2, value2 in new_hash_a2.items():
        if key2 not in new_hash_a1.keys():
            return ('No')
        elif value2 > new_hash_a1[key2]:
            return ('No')
    return ('Yes')


a1 = [11, 7, 1, 13, 21, 3, 7, 3]
# a1 = [10, 5, 2, 23, 19]
a2 = [11, 3, 7, 1, 7]
# a2 = [19, 5, 3]
n = 8
m = 5
res = isSubset(a1, a2, n, m)
print(res)
