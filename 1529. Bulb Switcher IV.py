def minFlips(self, target: str) -> int:
        #return len(list(groupby("0" + target)))-1  # 1-Liner Sol
        
        #c=0  # My Sol
        #key = 1
        #for i in target:
         #   if(int(i)==key):
          #      c+=1
           #     key=1-key
            
        c= 2 * target.count('10')  # Efficient Sol
        return  c+ 1 if target[-1] == '1' else c
