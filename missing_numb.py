# find the missing number in a sorted array
def missing_numb(arr):
    xor1 = 0
    xor2 = 0 
    for i in range(0,len(arr)+1):
        xor1 = xor1 ^ i 
    for j in range(0,len(arr)):
        xor2 = xor2 ^ arr[j] 
    
    return xor1 ^ xor2 

arr = [3,0,1]
res = missing_numb(arr)
print(res)
