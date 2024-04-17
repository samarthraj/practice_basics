# Given two arrays A[] and B[] of size n. It is given that both array individually contains distinct elements. We need to find the sum of all elements that are not common.
def function(a, b):
    new_list = a + b
    hashmap = {}
    out = 0

    for i in range(0, len(new_list)):
        if new_list[i] in hashmap:
            hashmap[new_list[i]] += 1
        else:
            hashmap[new_list[i]] = 1

    for keys, value in hashmap.items():
        if value == 1:
            out = out + keys
    return out

# a = [1, 5, 3, 8]
# b = [5, 4, 6, 7]


a = [1, 5, 3, 8]
b = [5, 1, 8, 3]

res = function(a, b)
print(res)
