def starting_ending(nums, target):
    low = 0
    high = len(nums) - 1
    lower_occurance = -1
    while low <= high:
        mid = (low+high) // 2
        if target == nums[mid]:
            lower_occurance = mid
            high = mid - 1 
        elif target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1

    return lower_occurance, ending(nums, target) 

def ending(nums, target): 
    low = 0
    high = len(nums) - 1
    high_occurance = -1
    while low <= high:
        mid = (low+high) // 2
        if target == nums[mid]:
            high_occurance = mid
            low = mid + 1 
        elif target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
    
    return high_occurance

arr = [5, 7, 7, 8, 8, 10]
target = 8
res = starting_ending(arr, target)
print(res) 
