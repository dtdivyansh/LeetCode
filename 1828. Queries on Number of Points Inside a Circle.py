def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x,y,r in queries:
            c=0
            for a,b in points:
                d = ( (x-a)**2 + (y-b)**2 )**(1/2)
                if(d<=r):
                    c+=1
            ans.append(c)
        
        return ans
