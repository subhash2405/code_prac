# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, temp, lower=float('-inf'), upper=float('inf')):
        if temp is None:
            return True

        if not (lower < temp.val < upper):
            return False
        return (
            self.valid(temp.left, lower, temp.val) and
            self.valid(temp.right, temp.val, upper)
        )

# https://leetcode.com/problems/validate-binary-search-tree/