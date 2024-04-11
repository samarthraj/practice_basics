#Print linearly from N to 1, by backtracking method, you use negative
def func(i,n):
    if (i > n):
        return
    func(i+1,n)
    print(i)    
    
i = 1
n = 5
res = func(i,n)
print(res)