#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        i=0
        def fun(preorder,mini,maxi,n):
            nonlocal i
            if(i>=n):
                return None
            else:
                if(mini < preorder[i] < maxi):
                    node = TreeNode(preorder[i])
                    key = preorder[i]
                    i+=1
                    node.left = fun(preorder,mini,key,n)
                    node.right = fun(preorder,key,maxi,n)
                    
                    return node
                else:
                    return None
                
        return fun(preorder,0,10**8+1,len(preorder))
