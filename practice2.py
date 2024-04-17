#Insertion Sort 
def merge_sort(arr):
#here we are breaking it into two lists and comparing the left most element of both the lists
    if len(arr) > 1: 
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    
        #do recurrsion 
        merge_sort(left_arr)
        merge_sort(right_arr)

        #do actual merge below
        i = 0 #left index 
        j = 0 #right index 
        k = 0 # merge index 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr

arr = [4,1,5,0,9,8,-67,-5]
res = merge_sort(arr)
print(arr)
