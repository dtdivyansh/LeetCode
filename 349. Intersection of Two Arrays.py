def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if(len(nums1)<len(nums2)):
            arr1 = nums1
            arr2 = nums2
        else:
            arr2 = nums1
            arr1 = nums2
            
        s1 = set(arr1)
        arr1 = list(s1)
        s1 = set(arr2)
        arr2 = list(s1)
        arr1.sort()
        ans = []
        l = len(arr1)
        for k in arr2:
            i = 0
            j = l-1
            while(i<=j):
                mid = (i+j)//2
                if(arr1[mid]==k):
                    ans.append(k)
                    break
                
                elif(arr1[mid]<k):
                    i = mid+1
                
                else:
                    j = mid-1
        return ans
