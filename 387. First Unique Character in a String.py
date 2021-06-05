def firstUniqChar(self, s: str) -> int:
        var = [i for i in s]
        flag=[]
        for i in range(len(var)):
            if(i == len(var)-1 and var[i] not in flag):
                return i
            
            if(var[i] in var[i+1:]):
                flag.append(var[i])
            elif(var[i] not in flag):
                return i
        return -1
