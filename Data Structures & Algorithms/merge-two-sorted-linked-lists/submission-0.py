# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        currentNode1 = list1
        currentNode2 = list2
        currentRes = dummy

        while currentNode1 or currentNode2:
            if not currentNode1:
                currentRes.next = currentNode2
                break

            if not currentNode2:
                currentRes.next = currentNode1
                break

            if currentNode1.val <= currentNode2.val:
                node = ListNode(val=currentNode1.val)
                # node.next = None

                currentRes.next = node
                currentNode1 = currentNode1.next
            else:
                node = ListNode(val=currentNode2.val)
                # node.next = None

                currentRes.next = node
                currentNode2 = currentNode2.next
            
            currentRes = currentRes.next

        return dummy.next
            




