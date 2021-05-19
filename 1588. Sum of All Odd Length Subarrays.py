def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        left = 0
        right = 3
        l = len(arr)
        s = sum(arr)
        if(l<right):
            return s
        
        while(right<=l):
            left1 = 0
            right1 = right
            while(right1<=l):
                s+=( sum(arr[left1:right1]) )
                left1+=1
                right1+=1
            right = right+2
        return s
