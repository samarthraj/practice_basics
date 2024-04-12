#Reverse a String 
def reverse_string(string):
    size = len(string)
    if (size == 0): 
        return 
    last_char = string[size-1]
    print(last_char, end ="") 
    reverse_string(string[:len(string)-1])
        
string = "Samarth"
res = reverse_string(string)

