#https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum([sum([int(j) for j in str(i)]) for i in nums]))
