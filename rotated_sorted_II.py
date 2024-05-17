def rotated_sorted(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return True
        elif nums[low] == nums[mid] and nums[high] == nums[mid]:
            low = low + 1
            high = high - 1
            continue
        elif nums[low] <= nums[mid]:
            if nums[low] <= target and nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[high] >= nums[mid]:
            if nums[high] >= target and nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
    return False


nums = [2, 5, 6, 0, 0, 0, 1, 2]
target = 0
res = rotated_sorted(nums, target)
print(res)
