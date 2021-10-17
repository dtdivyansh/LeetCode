# SOLUTION 1  (More Efficient)

def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = []
        for i in range(n):
            head,tail = i-1,i+1
            if(s[i]==c):
                ans.append(0)
            else:
                while(head>-1 or tail<n):
                    if(head>-1 and tail<n):
                        if(s[head]==c or s[tail]==c):
                            ans.append(abs(i-head))
                            break
                        else:
                            head-=1
                            tail+=1
                    elif(head>-1 and s[head]==c):
                        ans.append(abs(i-head))
                        break
                    elif(tail<n and s[tail]==c):
                        ans.append(abs(i-tail))
                        break
                    else:
                        if(head>-1):
                            head-=1
                        else:
                            tail+=1
        return ans
      
      
# SOLUTION 2

def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = []
        for i in range(len(s)):
            if(s[i]==c):
                arr.append(i)
        
        ans = []
        
        for i in range(len(s)):
            if(s[i]==c):
                ans.append(0)
            else:
                m = min(arr,key = lambda x:abs(x-i))
                ans.append(abs(m-i))
        
        return ans
