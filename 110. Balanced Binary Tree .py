# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


 

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root): 
            if root is None: 
                return 0
            left,right=getHeight(root.left),getHeight(root.right)
            if left<0 or right<0 or abs(left-right)>1: 
                return -1
            return max(left, right)+1
        return getHeight(root)!=-1