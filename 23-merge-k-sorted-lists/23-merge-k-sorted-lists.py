# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge2Lists(self, list1, list2):
        
        # create temp list:
        head = tx = ListNode(0)
        
        lx = list1
        rx = list2
        # if both lists are not empty:
        while lx and rx:
            if lx.val < rx.val:
                tx.next = ListNode(lx.val)
                lx = lx.next
            else:
                tx.next = ListNode(rx.val)
                rx = rx.next
            tx = tx.next
        
        # if left list is not empty:
        while lx:
            tx.next = ListNode(lx.val)
            lx = lx.next
            tx = tx.next
            
        # if right list is not empty:
        while rx:
            tx.next = ListNode(rx.val)
            rx = rx.next
            tx = tx.next
        
        return head.next
        
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) < 50:
            temp = lists[0]
            for ix in range(1, len(lists), 1):
                temp = self.merge2Lists(temp, lists[ix])
            return temp
        else:
            
            temp = {}
            for ix in range(25):
                temp[ix] = lists[ix]
            
            for ix in range(25):
                for i in range(ix+25, len(lists), 25):
                    temp[ix] = self.merge2Lists(temp[ix], lists[i])
            
            txx = temp[0]
            for i in range(1, 25):
                txx = self.merge2Lists(txx, temp[i])
                    
        return txx