def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        if(n!=0 and m!=0):
            while(i< m+n ):
                if(nums2[j]<nums1[i]):
                    nums1.insert(i,nums2[j])
                    nums1.pop()
                    j+=1
                    i+=1
                elif(i >= m+j and nums1[i]==0 ):
                    nums1[i] = nums2[j]
                    i+=1
                    j+=1
                else:
                    i+=1
                if(j>=n):
                    break
        elif(m==0):
            while(i<m+n):
                nums1[i] = nums2[j]
                i+=1
                j+=1
