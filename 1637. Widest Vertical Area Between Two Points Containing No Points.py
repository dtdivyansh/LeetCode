def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        c = 0
        for i in range(1,len(points)):
            c = max( c, points[i][0]-points[i-1][0] )
        return c
