# find peak element 
nums = [3,4,5,6,1,2]
left, right = 0, len(nums) - 1
while left < right:
    mid1  = (left + right) // 2
    mid2 = mid1 + 1
    if nums[mid1] > nums[mid2]:
        right = mid1
    else:
        left = mid2
print(nums[left])
            