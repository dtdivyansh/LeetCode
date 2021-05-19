def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            while(i>=0.1):
                if(i < 1 ):
                    c+=1
                    break
                i = i/100
               
        return c
