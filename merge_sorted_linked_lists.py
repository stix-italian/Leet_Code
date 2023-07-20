# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []
        print(list1.val)
        print(list2)
        if list1.val < list2.val:
            merged.append(list1.val)
            list1.next
        elif list1.val > list2.val:
            merged.append(list2.val)
        else:
            merged.extend([list1.val, list2.val])
        # for x in list1:
        #     for y in list2:
        #         if x < y:
        #             merged.append(x)
        #         elif y > x:
        #             merged.append(y)
        #         else:
        #             merged.extend(x,y)
        # return merged
