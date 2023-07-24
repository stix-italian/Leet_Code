# Took too long understanding how linked lists work in python. Lots of playing with print statements to understand how
# to access the val and next in the lists. Got my solution to start working but it's logic is flawed and just spits out
# [0,4] as the end combined list. So here is a Solution from the internet:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
# from typing import ListNode

# class Solution:
#     def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1 and not list2:
#             return list1
#         elif not list1:
#             return list2
#         elif not list2:
#             return list1
#         merged = ListNode()
#         while list1 and list2:
#             if list1.val < list2.val:
#                 merged.next = list1.val
#                 list1 = list1.next
#             elif list1.val > list2.val:
#                 merged.next = list2.val
#                 list2 = list2.next
#             else:
#                 merged.next = list1
#                 merged.next = list2
#                 list1, list2 = list1.next, list2.next
#         return merged
        
        
#     list1 = ListNode[val: 1, next: ListNode[val: 2, next: ListNode[val: 4, next: None]]]
#     list2 = ListNode[val: 1, next: ListNode[val: 3, next: ListNode[val: 4, next: None]]]
#     mergeTwoLists(list1, list2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # merged = []
        # print(list1.val)
        # print(list2)
        # if list1.val < list2.val:
        #     merged.append(list1.val)
        #     list1.next
        # elif list1.val > list2.val:
        #     merged.append(list2.val)
        # else:
        #     merged.extend([list1.val, list2.val])
        # for x in list1:
        #     for y in list2:
        #         if x < y:
        #             merged.append(x)
        #         elif y > x:
        #             merged.append(y)
        #         else:
        #             merged.extend(x,y)
        # return merged
