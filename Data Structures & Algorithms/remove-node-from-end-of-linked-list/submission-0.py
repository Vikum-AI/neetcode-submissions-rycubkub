# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        p1 = dummy
        p2 = dummy

        current_node = dummy
        count = 0

        while current_node:
            if not current_node.next:
                if p2.next.next:
                    p2.next = p2.next.next
                else:
                    p2.next = None

            current_node = current_node.next
            p1 = p1.next
            
            if count >= n:
                p2 = p2.next

            count += 1            

        return dummy.next

            

