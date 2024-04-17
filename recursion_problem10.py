#Find the nth element in a fibonacci series 
def fibonacci_nos(n):
    if n <= 1:
        return n
    last = fibonacci_nos(n-1) 
    second_last = fibonacci_nos(n-2)
    return last + second_last

n = 7
res = fibonacci_nos(n)
print(res)


