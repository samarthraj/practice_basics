#Check if its a palindrome using recursion 
def palindrome(i,string):
    n = len(string)
    if i >= n//2:
        return True
    if string[i].upper() != string[n-i-1].upper():
        return False
    return palindrome(i+1,string)

string = "Sam"
res = palindrome(0,string)
print(res)
