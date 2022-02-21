class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid1  = (left + right) // 2
            if nums[mid1] > nums[right]:
                left = mid1 + 1
            else:
                right = mid1
        # print(nums[left])
        def bsearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid  = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        # print(left)
        if left == 0:
            result = bsearch(nums, target)
            return result
        elif target >= nums[0] and target <= nums[left - 1]:
            result = bsearch(nums[:left], target)
            return result
        else:
            result = bsearch(nums[left:], target)
            if result != -1:
                result += left
            return result
            
            
                
        
            