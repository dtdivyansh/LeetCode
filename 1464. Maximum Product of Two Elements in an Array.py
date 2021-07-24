def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)


# Priority Queue Logic

import heapq as hq
def maxProduct(self, nums: List[int]) -> int:
        heap = []
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                hq.heappush(heap,(nums[i]-1)*(nums[j]-1)*(-1))
        return (-1)*hq.heappop(heap)
