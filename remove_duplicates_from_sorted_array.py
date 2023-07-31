
# failed to understand how to pop and go through a list at the same time. Iterating that way 
# you jump around too much. Example [1,1,2] if on pass 2 pop the second 1 the list is now length 2
# and the loop stops because you've already done 2 iterations even thos you haven't touched the 2.
from typing import List
class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        k = set()
        count = 0
        for x in range(0,len(nums)):
            if nums[x] in k:
                nums.append(nums.pop(x))
                x = x-1
            else: 
                k.add(nums[x])
                count +=1
        return count #len(nums)
        
    
    # tried nums = set(nums) but that doesn't updated the nums list element so when it's returned it looks like nothing changed.
    removeDuplicates([1,1,2])



# Solution from the internet..
    # i = 1
    # while i < len(nums):
    #     if nums[i] == nums[i - 1]:
    #         nums.pop(i)
    #     else:
    #         i += 1
    # return len(nums)