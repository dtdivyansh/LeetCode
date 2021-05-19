def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if(ruleKey=='type'):
            sel = 0
        elif(ruleKey=='color'):
            sel = 1
        else:
            sel = 2
        for item in items:
            if(item[sel]==ruleValue):
                count+=1
        return count
