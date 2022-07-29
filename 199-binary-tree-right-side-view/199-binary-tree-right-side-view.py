# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = deque([root])
        res = []
        while stack:
            lenQ = len(stack)
            right = None
            for i in range(lenQ):
                node = stack.popleft()
                #right = None
                #print right
                if node:
                    right = node
                    stack.append(right.left)
                    stack.append(right.right)
            
            if right:
                #print right.val
                res.append(right.val)
        return res
                