def rotate_by_k(arr, k):
    n = len(arr) 
    k = k % n 

    #so now you rotate k times ex: n = 5, k = 12, then k % n = 2, u rotate u times equivalent ans 
    roatted_array = arr[k:] + arr[:k]
    #return rotated_array = arr[k:] + arr[:k]
    return roatted_array

arr = [1, 2, 3, 4, 5]
k = 3
res = rotate_by_k(arr, k)
print(res)
