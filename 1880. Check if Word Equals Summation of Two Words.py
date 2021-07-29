def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def fun(s,dic):
            n = ''
            for i in s:
                n = n + str(dic[i])
            return int(n)
        
        dic = {}
        k = 0
        
        for i in 'abcdefghijklmnopqrstuvwxyz':
            dic[i] = k
            k+=1
        
        a = fun(firstWord,dic)
        b = fun(secondWord,dic)
        c = fun(targetWord,dic)
        
        if(a+b==c):
            return True
        return False
