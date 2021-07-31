def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        c=0
        for i in groupSizes:
            if(i in dic.keys()):
                if( len(dic[i][-1]) >= i ):
                    dic[i].append([c])
                    c+=1
                else:
                    dic[i][-1].append(c)
                    c+=1
            else:
                dic[i] = [[c]]
                c+=1
        
        ans = []
        for i in dic.values():
            ans.extend(i)
        
        return ans
