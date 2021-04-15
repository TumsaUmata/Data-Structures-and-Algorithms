class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_than_x, not_less_than_x = ListNode(0), ListNode(0)
        less_than_x_head, not_less_than_x_head, current = less_than_x, not_less_than_x, head
        while current:
            if current.val < x:
                less_than_x_head.next = current
                less_than_x_head = current
            else:
                not_less_than_x_head.next = current
                not_less_than_x_head = current
            current = current.next
        less_than_x_head.next, not_less_than_x_head.next = not_less_than_x.next, None
        return less_than_x.next
