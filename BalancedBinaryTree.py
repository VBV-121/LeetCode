# Given a binary tree, determine if it is height-balanced

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        def findheight(node):
            if node is None:
                    return 1
            dr = findheight(node.right)
            if dr == 0:
                return 0
            dl = findheight(node.left)
            if dl == 0:
                return 0
            if abs(dr-dl) > 1:
                return 0
            return max(dr,dl)+1
        return findheight(root) != 0