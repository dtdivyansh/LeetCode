def partitionLabels(self, s: str) -> List[int]:
        l = len(s)
        i,j = 0,l-1
        last,ans,stack = j,[],{}
        
        while(i<l):
            if(s[i] not in stack.keys()):
                val = s[i]
                stack[val] = 1
            else:
                i+=1
                continue

            j = s.rindex(val)    
            if(j==i):
                ans.append(1)
                i+=1
                j = last
                continue
            else:
                m,st = j,i
                i+=1
                j = last
                    
                while(i<m):
                    val = s[i]
                    if(val in stack.keys()):
                        i+=1
                        continue
                    else:
                        stack[val] = 1
                        
                    j = s.rindex(val)        
                    m = max(j,m)
                    i+=1
                    j = last
                
                ans.append(m-st+1)
                j = last    
                i = m+1
            
        return ans
