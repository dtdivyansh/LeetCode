def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for i in sentence:
            dic[i] = 1
            
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if(i not in dic.keys()):
                return False
        return True
