from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # first get rid of all the 0's added as place holders in list 1
        for x in range (0,n):
            nums1.pop()
        # combine lists and then sort.
        nums1.extend(nums2)
        nums1.sort()