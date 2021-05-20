def minOperations(self, boxes: str) -> List[int]:
        left = right = lcost = rcost = 0
        n = len(boxes)
        ans = [0]*n
        for i in range(1,n):
            if(int(boxes[i-1])):
                left+=1
            lcost+=left
            ans[i]=lcost
            
        for i in range(n-2,-1,-1):
            if(int(boxes[i+1])):
                right+=1
            rcost+=right
            ans[i]+=rcost
                    
        return ans
