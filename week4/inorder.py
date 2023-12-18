# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root,ans):
            if root:
                inorder(root.left,ans)
                ans.append(root.val)
                inorder(root.right,ans)
        ans=[]
        inorder(root,ans)
        return ans

        # https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=daily-question&envId=2023-12-09