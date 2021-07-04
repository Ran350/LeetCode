#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        merged_head = merged = ListNode()

        while (l1 and l2):
            if(l1.val <= l2.val):
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next

        if(l1):
            merged.next = l1
        if(l2):
            merged.next = l2

        return merged_head.next


# @lc code=end
