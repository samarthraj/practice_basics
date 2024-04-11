#Print linearly from 1 to N
def func(i,n):
    #base condition 
    if i > n:
        return
    print(i)
    #recursion function call 
    func(i+1,n)
    
i = 1
n = 5
res = func(i,n)
print(res)

