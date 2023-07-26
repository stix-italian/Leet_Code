from typing import List
class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        while nums:
            x = nums.pop(0)
            if x in nums:
                return True
        return False
    

    print(containsDuplicate([1,2,3,4]))

# While loop ended up taking too long to calculate their test case of -24000 to positive 29000 with no duplicates. 
# The online solutions I looked at mentioned using sets, since sets can't have any duplicates. the simplest answer
# just did set(nums) and then compared the length of nums vs set(nums) because turning nums into a set will skip 
# over the duplicates causing differnt lengths. The answer I chose to submit was closer to my original answer.
# iterating over nums instead of doing a while loop is faster and passed all the test cases. 

# num_set = set()
# for i in nums:
#     if i in num_set:
#         return True
#     else:
#         num_set.add(i)