def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = nums
        arr.sort()
        ans = []
        for i in range(len(arr)):
            head=i+1
            tail = len(arr)-1
            while(head<tail):
                val = arr[i]+arr[head]+arr[tail]
                if(val==0):
                    res = [arr[i],arr[head],arr[tail]]
                    if(res not in ans):
                        ans.append(res)
                    head+=1
                    tail-=1
                elif(val<0):
                    head+=1
                else:
                    tail-=1
            
        ans.sort()
        return ans
