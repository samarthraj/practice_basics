#Print linearly from N to 1
def func(i,n):

    if (i > n):
        return 
    print(n)
    func(i,n-1)
    
i = 1
n = 5
res = func(i,n)
print(res)

