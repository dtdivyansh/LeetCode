#https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum, rightsum = [], []
        l = len(nums)
        left = 0
        for i in range(l):
            leftsum.append(left)
            left += nums[i]

        right = 0
        for i in range(l-1, -1, -1):
            rightsum.insert(0,right)
            right += nums[i]

        return[abs(leftsum[i] - rightsum[i]) for i in range(l)]
