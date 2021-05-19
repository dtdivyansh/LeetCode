def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        last = len(mat)-1
        start = 0
        for row in mat:
            s += (row[start] + row[last])
            if(start==last):
                s-=row[start]
            last-=1
            start+=1
        return s
