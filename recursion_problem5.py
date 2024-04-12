#Sum of first N numbers, functional way - means break it down into small functions so that it calls and gives results 
# def sum_of_n(i):
#     if i == 0: 
#         return 0 
#     return i + sum_of_n(i-1)

# n = 3
# res = sum_of_n(n)
# print(res)


#this is the parameterised way of doing a sum of n numbers using recursion, i.e. we use parameters 
def sum_of_n(i, sum):
    if i < 0: 
        print(sum)
        return 
    sum_of_n(i-1, sum+i)

n = 3
sum = 0
res = sum_of_n(n, sum)
print(res)



