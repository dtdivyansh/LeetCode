def lengthOfLongestSubstring(self, s: str) -> int:
        S = s
        size = len(S)
        if(s==''):
            return 0
        head = 0
        tail = 1
        m = 0
        while(tail<size):
            stri = S[head:tail]
            #print('STRING: ',stri,S[tail])
            if(S[tail] not in stri):
                #print(head,tail,stri,S[tail])
                l = len(S[head:tail+1])
                tail+=1
                if(l>m):
                    #print('sel ',S[head:tail])
                    m = l
            else:
                ind = S[head:tail].index(S[tail]) + len(S[0:head])
                head = ind+1
                tail+=1
        if(m==0):
            return 1
        return m
