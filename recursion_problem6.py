#Factorial of N, fucntional way
def factorial(i):

    if i == 1:  #also works with i == 0
        return 1
    return i*factorial(i-1)

n = 5
res = factorial(n)
print(res)