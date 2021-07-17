def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        c = 0
        i = 0
        pro = difficulty
        worker.sort()
        l = len(difficulty)
        for j in range(l):
            pro[j] = [pro[j],profit[j]]
        pro.sort()
        m = pro[i][1] if pro[i][0]<=worker[0] else 0
        for w in worker:
            while(i<l):
                if(pro[i][0]<=w):
                    m = max(m,pro[i][1])
                    i+=1
                else:
                    break
            if(i==l):
                i-=1
            c = c + m
        return c
