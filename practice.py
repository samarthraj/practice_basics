##Factorial of N 
# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1) 

# n = 5
# res = factorial(n)
# print(res)

# #Sum of n numbers using recursion
# def sum_of_n(n):

#     if n == 0:
#         return 0
#     return n + sum_of_n(n-1)
    
# n = 3
# res= sum_of_n(n)
# print(res)

# #Reverse a String using recursion 
# def reverse_string(str):
#     n = len(str)
#     if n == 0:
#         return
#     print(str[n-1], end = "")
#     reverse_string(str[:n-1]) 
    
# str = 'SAMA'
# res = reverse_string(str)
# #print(res)

# #Reverse a list using recursion 
# def reverse_list(ls):

#? 

# ls = [2,4,6,1,7]
# res = reverse_list(ls)
# print(res)

#Check for Palindrome using recursion 
def Palindrome(i,str):

    n = len(str)
    if i >= n//2:
        return True
    if str[i] != str[n-i-1]:
        return False 
    return Palindrome(i+1,str) 

str = 'SAMAS'
res = Palindrome(0,str)
print(res)





