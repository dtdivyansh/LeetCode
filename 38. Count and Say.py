def recFun(self,val,x):
            if(x<1):
                return val
            i=0
            temp=""
            while(i<len(val)):
                k=i
                c=0
                while(k<len(val) and val[i]==val[k]):
                    c+=1
                    k+=1
                temp=temp+str(c)+val[i]
                i=k
            return self.recFun(temp,x-1)
    
def countAndSay(self, n: int) -> str:
      return self.recFun("1",n-1)
