def single_element_sorted_array(nums):
    # the logic is to check for indexes
    # if there is a single number to the left of that number the indexes are odd even, but to the right of that number its odd and then even
    low = 0
    high = len(nums) - 1
    n = len(nums)
    if len(nums) == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]

    while low <= high:
        mid = (low+high)//2
        if nums[mid] != nums[mid+1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        else:
            nums[mid] == nums[mid+1]
            # means even index for the first one, the numb is on thr right side
            if ((mid) % 2 == 0) and nums[mid] == nums[mid - 1] or ((mid) % 2 != 0) and nums[mid] == nums[mid + 1]:
                high = mid - 1
            # the next one is even, the number is on the left side
            elif ((mid) % 2 != 0) and nums[mid] == nums[mid - 1] or ((mid) % 2 == 0) and nums[mid] == nums[mid + 1]:
                low = mid + 1


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1,1,2,3,3,4,4,8,8]
# [0,1,2,3,4,5,6,7,8]
res = single_element_sorted_array(nums)
print(res)
