def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1,m+1)]
        res = []
        
        for key in queries:
            ind = P.index(key)
            res.append(ind)
            val = P.pop(ind)
            P.insert(0,val)
            
        return res
