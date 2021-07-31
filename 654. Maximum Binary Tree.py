# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if(n==0):
            return None
        i = nums.index(max(nums))
        if(i>0):
            l = self.constructMaximumBinaryTree(nums[:i])
        else:
            l = None
        if(i<n-1):
            r = self.constructMaximumBinaryTree(nums[i+1:])
        else:
            r = None
            
        node = TreeNode(nums[i],l,r)
        return node
