# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    dic = {}
    def __init__(self, root: Optional[TreeNode]):
        self.dic = {}
        def fun(root):
            if(root==None):
                return -1
            if(root.left!=None):
                root.left.val = root.val*2+1
                self.dic[root.left.val]=1
            if(root.right!=None):
                root.right.val = root.val*2+2
                self.dic[root.right.val]=1
            if(root.left==None and root.right==None):
                return -1
            fun(root.left)
            fun(root.right)
                
        root.val = 0
        self.dic[root.val]=1
        fun(root)
        

    def find(self, target: int) -> bool:
        if(target in self.dic):
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
