"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        rec = {}
        temp = head
        original_values = []
        
        count = 0
        while temp != None:
            original_values.append(temp.val)
            temp.val = count
            rec[temp.val] = Node(temp.val)
            temp = temp.next
            count = count + 1

        
        temp = head
        while temp != None:
            if temp.next:
                rec[temp.val].next = rec[temp.next.val]
            if temp.random:
                rec[temp.val].random = rec[temp.random.val]
            temp = temp.next
        
        count = 0
        temp = rec[head.val]
        while temp != None:
            temp.val = original_values[count]
            temp = temp.next
            count = count + 1
        
        return rec[head.val]