#https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i,j = 0, len(s)-1
        s = [k for k in s]
        while i<j:
            if s[i] != s[j]:
                if s[i] < s[j]:
                    s[j] = s[i]
                else:
                    s[i] = s[j]
            i+=1
            j-=1
        
        return ''.join(s)
