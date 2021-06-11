def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed = set(allowed)
        for s in words:
            c = len(s)
            for i in s:
                if(i in allowed):
                    c-=1
                else:
                    break
            if(not c):
                res+=1
        return res
