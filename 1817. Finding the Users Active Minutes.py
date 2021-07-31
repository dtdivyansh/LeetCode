def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = {}
        
        for i,job in logs:
            if( i in dic.keys()):
                dic[i].add(job)
            else:
                dic[i] = set([job])
        
        ans = [0 for i in range(k)]
        
        for v in dic.values():
            ans[len(v)-1]+=1
        
        return ans
