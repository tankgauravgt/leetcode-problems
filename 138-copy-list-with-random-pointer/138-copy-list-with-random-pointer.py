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
        
        # fake label nodes:
        labels = {}
        
        cnt = 0
        temp = head
        while temp:
            labels[cnt] = temp.val
            temp.val = cnt
            temp = temp.next
            cnt = cnt + 1
        
        nodes = {}
        for ix in labels:
            nodes[ix] = Node(ix)

        temp = head
        while temp:
            if temp.next:
                nodes[temp.val].next = nodes[temp.next.val]
            if temp.random:
                nodes[temp.val].random = nodes[temp.random.val]
            temp = temp.next
        
        for ix in labels:
            nodes[ix].val = labels[ix]
        
        return nodes[head.val]