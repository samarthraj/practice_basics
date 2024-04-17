# Given two sets represented by two arrays, how to check if the given two sets are disjoint or not? It may be assumed that the given arrays have no duplicates.

def function(set1, set2):
    hashmap_set1 = {}
    for i in range(0, len(set1)):
        if set1[i] not in hashmap_set1:
            hashmap_set1[set1[i]] = 1

    for j in range(0, len(set2)):
        if set2[j] in hashmap_set1.keys():
            return ('Not Disjoint')
    return ('Disjoint')


set1 = [12, 34, 11, 9, 3]
set2 = [2, 1, 5, 4]
res = function(set1, set2)
print(res)
