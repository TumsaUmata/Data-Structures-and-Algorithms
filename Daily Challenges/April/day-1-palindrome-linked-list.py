# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = slow
        slow = slow.next
        prev.next = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        front = head
        back = prev

        while back:
            if front.val != back.val:
                return False
            front, back = front.next, back.next

        return True
