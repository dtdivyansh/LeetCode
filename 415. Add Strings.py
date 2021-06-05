def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        ans=""
        if(len(num1) > len(num2)):
            i=len(num1)-len(num2)
            num2="0"*i+num2
        else:
            i=len(num2)-len(num1)
            num1="0"*i+num1
            
        for j in range(len(num2)-1,-1,-1):
            temp= str( int(num1[j])+int(num2[j])+carry )
            if(len(temp)==2):
                carry=int(temp[0])
                temp=temp[1]
            else:
                carry=0
            ans=temp+ans
        if(carry!=0):
            ans=str(carry)+ans
        return ans
