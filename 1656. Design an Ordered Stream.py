def __init__(self, n: int):
        self.n = n+1
        self.prev = 1
        self.temp = [None]*(n+1)

def insert(self, idKey: int, value: str) -> List[str]:
        self.temp[idKey] = value
        if(idKey!=self.prev):
            return []
        
        l = []
        while( self.prev < self.n and self.temp[self.prev] is not None):
            l.append(self.temp[self.prev])
            self.prev+=1
        return l
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
