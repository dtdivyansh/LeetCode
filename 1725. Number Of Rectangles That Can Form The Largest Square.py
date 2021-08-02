def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a = [min(i) for i in rectangles]
        '''
        c=1
        m=a[0]
        for i in range(1,len(a)):
            if(a[i]==m):
                c+=1
            elif(a[i]>m):
                c=1
                m=a[i]
        return c
        '''
        m = max(a)
        return a.count(m)
