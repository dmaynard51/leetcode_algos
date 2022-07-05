# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.lst = []
        
        node = root
        
        self.creation(root)
    
    def creation(self, node):
        while node is not None:
            self.lst.append(node)
            node = node.left
    def next(self):
        """
        :rtype: int
        """
        node = self.lst.pop()
        
        self.creation(node.right)
        return node.val
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.lst
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()