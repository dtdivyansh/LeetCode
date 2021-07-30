def sortByBits(self, arr: List[int]) -> List[int]:
        dic = {}
        ans = []
        for i in arr:
            b = str(bin(i))
            c = b.count('1')
            if(c in dic.keys()):
                dic[c].append(i)
            else:
                dic[c] = [i]
        
        k = sorted(list(dic.keys()))
        for key in k:
            val = dic[key]
            ans.extend(sorted(val))
        
        return ans
