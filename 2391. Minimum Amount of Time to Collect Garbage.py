#https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        truck = {'M':[0,-1], 'G': [0,-1], 'P': [0,-1]}
        travel_time = [0]
        for i in range(len(travel)):
            travel_time.append(travel[i] + travel_time[i])

        for j in range(len(garbage)):
            kind = garbage[j]
            for key in 'MGP':
                if key in kind:
                    c = kind.count(key)
                    truck[key][0] += c
                    truck[key][1] = j

        ans = 0
        for key in 'MGP':
            ans += (truck[key][0] + travel_time[truck[key][1]]) if truck[key][1]>-1 else 0
        return ans  


# OPTIMISED

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = len(''.join(garbage))
        m,g,p = True, True, True
        for i in range(len(garbage) -1,-1,-1):
            gar = garbage[i]
            if 'M' in gar and m:
                ans+= sum(travel[:i])
                m=False
            if 'G' in gar and g:
                ans+= sum(travel[:i])
                g=False
            if 'P' in gar and p:
                ans+= sum(travel[:i])
                p=False
        
        return ans
