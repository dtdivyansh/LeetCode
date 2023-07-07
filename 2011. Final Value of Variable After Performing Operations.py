#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        mp = {"X++": 1, "++X":1, "--X": -1, "X--": -1}
        x = 0
        for op in operations:
            x += mp[op]
        return x
