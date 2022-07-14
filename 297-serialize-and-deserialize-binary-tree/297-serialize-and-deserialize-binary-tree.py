# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        nodes = []
        def preorder(node):
            nonlocal nodes
            if not node:
                nodes.append('x')
                return
            nodes.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return " ".join(nodes)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def preorder(nodes):
            val = next(nodes)
            if val == 'x': return
            cx = TreeNode(int(val))
            cx.left = preorder(nodes)
            cx.right = preorder(nodes)
            return cx
        
        return preorder(iter(data.split()))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))