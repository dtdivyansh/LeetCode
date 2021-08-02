def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if(s%3!=0):
            return False
        p = s//3
        v=0
        c=0
        for i in arr:
            v+=i
            if(v==p):
                c+=1
                v=0
        
        return c>=3
