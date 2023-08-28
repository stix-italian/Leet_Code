class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        pop_list = []
        for x in reversed(range(0,len(nums))):
            if nums[x] == val:
                nums.pop(x)   


# had to reverse the list as it was throwing out of index errors from popping. Also could have popped and appended to the back.
# that would have kept the list size the same while still popping in place.

# first passed solution
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = len(nums)
#         pop_list = []
#         for x in range(0,len(nums)):
#             if nums[x] == val:
#                 pop_list.append(x)

#         for y in reversed(pop_list):
#             nums.pop(y)
                
                