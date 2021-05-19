def runningSum(self, nums: List[int]) -> List[int]:
        if(not nums):
            return []
        running = [nums[0]]
        for i in range(1,len(nums)):
            running.append(running[i-1] + nums[i])
        return running
