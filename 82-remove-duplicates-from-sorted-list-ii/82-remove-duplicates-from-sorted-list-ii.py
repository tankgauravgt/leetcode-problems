# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def __init__(self):
        self.rec = {}
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        if head.next == None:
            return head
        
        temp = head       
        while temp != None:
            
            if temp.val not in self.rec:
                self.rec[temp.val] = 1
            else:
                self.rec[temp.val] += 1
            
            temp = temp.next
        
        hx = out = ListNode(None, None)
        for k, v in self.rec.items():
            if v == 1:
                out.next = ListNode(k)
                out = out.next
        
        return hx.next