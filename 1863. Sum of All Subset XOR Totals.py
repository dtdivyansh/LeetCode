    def subsetXORSum(self, nums: List[int]) -> int:
        
        def fun(nums,n,x):
            if(n<0):
                return x
            
            b=fun(nums,n-1,x^nums[n])
            c=fun(nums,n-1,x)
            #print(nums[n],b,c)
            return b+c
        
        a = fun(nums,len(nums)-1,0)
        #print(a)
        return a
