def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        destination = set()
        
        for s,d in paths:
            source.add(s)
            destination.add(d)
            
        res = list(destination-source)
        return res[0]
