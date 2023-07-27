from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = set()
        for x in nums:
            if x in k:
                nums.pop(x)
            else: 
                k.add(x)
        return len(nums)
    
    # tried nums = set(nums) but that doesn't updated the nums list element so when it's returned it looks like nothing changed.