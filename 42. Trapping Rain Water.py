# Trapping Rain Water

def trap(self, height: List[int]) -> int:
        n = len(height)
        
        rm = 0
        r = []
        for i in range(n-1,-1,-1):
            if(rm<=height[i]):
                rm = height[i]
                r.insert(0,0)
            else:
                r.insert(0,rm)
        v=0
        lm = 0
        l = []
        for i in range(n):
            if(lm<=height[i]):
                lm = height[i]
                l.append(0)
            else:
                l.append(lm)
            m = min(l[i],r[i])
            if(m):
                v = v + m - height[i]
        
        return v
        
