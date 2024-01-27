"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1 or list2:
            tail.next = list1 if list1 else list2

        return dummy.next


s = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

l1 = a1
a1.next = a2
a2.next = a3

l2 = b1
b1.next = b2
b2.next = b3

res = s.mergeTwoLists(l1, l2)
print('end')
