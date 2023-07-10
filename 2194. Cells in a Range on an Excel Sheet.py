#https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = []
        cell1, cell2 = s.split(':')
        c1, c2, r1, r2 = cell1[0], cell2[0], int(cell1[1]), int(cell2[1])
        i, j = alpha.index(c1), alpha.index(c2)
        while i <= j:
            for k in range(r1, r2+1):
                ans.append(alpha[i]+str(k))
            i+=1
        
        return ans
