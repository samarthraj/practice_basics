#
def insert(nums, target):
    low = 0
    high = len(nums) - 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            ans = mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


nums = [1, 3, 5, 6]
target = 2
res = insert(nums, target)
print(res)
