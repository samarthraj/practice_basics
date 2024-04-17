# Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.
def hasArrayTwoCandidates(arr, x):
    hashmap = {}

    for i in range(0, len(arr)):
        temp = x - arr[i]
        if (temp in hashmap):
            return 'Yes'
        hashmap[arr[i]] = i
    return 'No'

arr = [1, 2, 4, 3, 6]
#arr = [335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36,895, 704, 812, 323, 334]
#x = 468
x = 10
res = hasArrayTwoCandidates(arr, x)
print(res)
