# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        curr=root
        self.inorder(root,res)
        return res[k-1]

    def inorder(self,temp,res):
        if temp is not None:
            self.inorder(temp.left,res)
            res.append(temp.val)
            self.inorder(temp.right,res)


# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/