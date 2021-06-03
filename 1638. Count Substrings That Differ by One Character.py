def countSubstrings(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        A, B = [0]*(n+1), [0]*(n+1)
        ans = 0
        for i in range(m):
            AA, BB = [0]*(n+1), [0]*(n+1)
            for j in range(n):
                AA[j+1] = 1 + A[j] if s[i]==t[j] else 0
                BB[j+1] = B[j] if s[i]==t[j] else 1 + A[j]
                ans += BB[j+1]
            A, B = AA, BB
        return ans
