def findPeakElement(self, nums: List[int]) -> int:
        def find(arr,i,j,n):
            if(n==1):
                return 0
            while(i<=j):
                mid = (i+j)//2
                if(mid==0):
                    if(arr[0]>arr[1]):
                        return 0
                    else:
                        return 1
                if(mid==n-1):
                    if(arr[mid]>arr[n-2]):
                        return n-1
                    else:
                        return n-2
                if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                    return mid
                else:
                    if(arr[mid+1]>arr[mid]):
                        i = mid+1
                    else:
                        j = mid-1
        n = len(nums)
        return find(nums,0,n-1,n)
