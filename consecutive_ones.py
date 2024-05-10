# max consecutive ones
def consecutive_ones(arr):
    sum_ones = 0
    maximum_ones = 0
    for i in range(0, len(arr)):
        if arr[i] == 1:
            sum_ones += 1
            maximum_ones = max(sum_ones, maximum_ones)
        else:
            sum_ones = 0
    return maximum_ones


arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
res = consecutive_ones(arr)
print(res)
