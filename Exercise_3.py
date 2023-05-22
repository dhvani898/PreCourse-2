# Python program for implementation of Find Mid Point of a Singly Linked List.
# https://leetcode.com/problems/middle-of-the-linked-list/
# Time Complexity: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1=head
        curr2=head
        while(curr2 and curr2.next):
            curr2=curr2.next.next
            curr1=curr1.next
        return curr1

        