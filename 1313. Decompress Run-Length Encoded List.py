def decompressRLElist(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(0,len(nums),2):
            final+=( nums[i]*[nums[i+1]] )
        return final
