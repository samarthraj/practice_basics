# ceil the floor
def getFloorAndCeil(a, n, x):
    low = 0
    high = n - 1
    floor = -1
    ceil = -1
    while low <= high: 
        mid = (low+high)//2 
        if a[mid] >= x: 
            ceil = a[mid] 
            high = mid - 1
            
        elif a[mid] <= x: 
            floor = a[mid] 
            low = mid + 1 
        
    return floor, ceil 
        

n = 6
x = 8
a = [3, 4, 7, 8, 8, 10] 
res = getFloorAndCeil(a, n, x)
print(res)
