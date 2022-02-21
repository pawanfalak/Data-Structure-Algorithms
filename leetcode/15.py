class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        size = len(nums)
        result = set()
        count = {}
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        for i in range(0, size - 1):
            count[nums[i]] -= 1
            for j in range(i+1, size):
                count[nums[j]] -= 1
                if -nums[i]-nums[j] in count:
                    if count[-nums[i]-nums[j]] > 0:
                        candidate = [nums[i], nums[j], -nums[i]-nums[j]]
                        candidate.sort()
                        result.add(tuple(candidate))
                count[nums[j]] += 1
            count[nums[i]] += 1
                    
        return list(result)