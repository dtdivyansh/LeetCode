def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''.join( word1[i:i+1] + word2[i:i+1] for i in range(100) )
        return res
