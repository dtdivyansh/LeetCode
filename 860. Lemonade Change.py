def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0, 10:0}
        
        for i in bills:
            if(i==5):
                dic[i]+=i
            else:
                if(i==10):
                    if(dic[5]>=5):
                        dic[5]-=5
                        dic[10]+=10
                    else:
                        return False
                else:
                    if(dic[5]>=5 and dic[10]>=10):
                        dic[5]-=5
                        dic[10]-=10
                    elif(dic[5]>=15):
                        dic[5]-=15
                    else:
                        return False
        return True
