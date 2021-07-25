def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score)
        c = 1
        ans = []
        l = len(arr)-1
        dic = {}
        for i in range(l,-1,-1):
            if(c==1):
                dic[arr[i]] = "Gold Medal"
                c+=1
            elif(c==2):
                dic[arr[i]] = "Silver Medal"
                c+=1
            elif(c==3):
                dic[arr[i]] = "Bronze Medal"
                c+=1
            else:
                dic[arr[i]] = str(c)
                c+=1
        
        for i in score:
            s = dic[i]
            ans.append(s)
            
        return ans
