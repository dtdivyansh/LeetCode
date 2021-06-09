def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = ''
        banned = set(banned)
        for i in paragraph:
            if(i==' ' or i.isalpha()):
                para+=i.lower()
            else:
                para+=' '
        dic = {}
        arr = para.split(' ')
        m = 0
        key = ''
        for i in arr:
            if(i in dic):
                dic[i]+=1
                if(dic[i]>m):
                    m=dic[i]
                    key = i
            elif(i not in banned and i.isalpha()):
                dic[i]=1
                if(dic[i]>m):
                    m=dic[i]
                    key = i
                
        return key
