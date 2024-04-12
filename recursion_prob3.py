#Print linearly from 1 to N, by backtracking method, you use negative
def func(i,n):

    if (i < 1):
        return
    func(i-1,n)
    print(i)    

i = 5
n = 5
res = func(i,n)
print(res)


