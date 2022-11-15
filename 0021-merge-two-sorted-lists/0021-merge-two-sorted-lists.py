# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p = head = ListNode()
        
        while list1 and list2:
            
            if list1.val<=list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
                
            p = p.next
            
        
        if list1 or list2:
            p.next = list1 if list1 else list2
            
        return head.next
            
            
            