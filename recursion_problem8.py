#Reverse a String 
def reverse_string(string):

    size = len(string)
    if size == 0: 
        return 
    last_str = string[size-1] 
    print(last_str, end = "")
    reverse_string(string[:len(string)-1])

string = "WEEK"
res = reverse_string(string)

