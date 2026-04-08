class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        n = len(nums)
        for i in range(0,n):
            d[nums[i]]=d.get(nums[i],0)+1
        
        for i in nums:
            if d[i] > 1:
                return True
    
        return False