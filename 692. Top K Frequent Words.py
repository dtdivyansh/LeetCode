def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic ={}
        s =set(words)
        s = sorted(list(s))
        size=0
        for i in s:
            c = words.count(i)
            if(c in dic.keys()):
                dic[c].append(i)
            else:
                dic[c]=[i]
        
        key = sorted(list(dic.keys()),reverse=True)
        ans = []
        for p in key:
            for i in dic[p]:
                ans.append(i)
                size+=1
                if(size==k):
                    return ans
