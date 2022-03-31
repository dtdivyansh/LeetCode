class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = {}
        items = set()
        for ord in orders:
            it = ord[2]
            items.add(it)
            t = int(ord[1])
            if(t in table):
                if(it in table[t]):
                    table[t][it]+=1
                else:
                    table[t][it]=1
            else:
                table[t] = {it:1}
        
        item = list(items)
        item.sort()
        tab = sorted(table)
        
        first = [i for i in item]
        first.insert(0,'Table')
        ans = [first]
        for i in tab:
            sec = [str( table[i][j] ) if j in table[i] else '0' for j in item ]
            sec.insert(0,str(i))
            ans.append(sec)
        
        return ans
