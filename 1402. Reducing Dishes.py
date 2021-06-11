def maxSatisfaction(self, satisfaction: List[int]) -> int:
        dic = {}
        def solve(arr,i,j,total):
            if( (i,j) in dic.keys() ):
                return dic[(i,j)]
            if(i<0):
                return total
            else:
                like = total + arr[i]*j
                
                a = max( solve(arr,i-1,j,total) , solve(arr,i-1,j+1,like) )
                dic[(i,j)] = a
                
                return a
            
        satisfaction.sort(reverse=True)
        l = len(satisfaction)-1
        ans = solve(satisfaction,l,1,0)
        return ans
