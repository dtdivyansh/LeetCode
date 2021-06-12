def letterCombinations(self, digits: str) -> List[str]:
        
        def solve(dic,digits):
            if(len(digits)==1):
                ans = [i for i in dic[digits]]
                return ans
            else:
                r = digits[0]
                ans = []
                val = solve(dic,digits[1:])
                for s in dic[r]:
                    for p in val:
                        ans.append(s+p)
                return ans
                    
        if(digits==""):
            return []
        
        else:
            dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
            ans = solve(dic,digits)
            return ans
