def longestCommonPrefix(self, strs: List[str]) -> str:
        val=""
        if not strs:
            return val
        ref=strs[0]
        for i in range(len(strs[0])):
            for j in strs:
                if(i>=len(j) or ref[i]!=j[i]):
                    return val
            val+=ref[i]
        return val
