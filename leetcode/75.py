# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        def quicksort(start, end):
            if start >= end:
                return
            pivot, index = nums[end], start
            for i in range(start, end):
                if nums[i] < pivot:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
            nums[end], nums[index] = nums[index], nums[end]    
            quicksort(start, index - 1)
            quicksort(index + 1, end)
        quicksort(0, size - 1)