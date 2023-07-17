#https://leetcode.com/problems/uncrossed-lines/

def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        def lcs(m,n,X,Y):
            nonlocal dp
            if(m==0 or n==0):
                return 0
            elif((m,n) in dp.keys() ):
                return dp[(m,n)]
        
            elif( X[m-1] == Y[n-1] ):
                dp[(m,n)] =  1 + lcs(m-1,n-1,X,Y)
                return dp[(m,n)]
            else:
                dp[(m,n)]= max( lcs(m,n-1,X,Y) , lcs(m-1,n,X,Y) )
                return dp[(m,n)]
        
        return lcs(len(nums1),len(nums2),nums1,nums2)
