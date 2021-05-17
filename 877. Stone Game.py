# Stone Game

def stoneGame(self, piles: List[int]) -> bool:
        def stone(piles,i,j):
            if(j-i==1):
                return max(piles[i],piles[j])
            else:
                c = 0
                if(piles[i]>piles[j]):
                    c = piles[i] + stone(piles,i+1,j)
                elif(piles[i]<piles[j]):
                    c = piles[j] + stone(piles,i,j-1)
                else:
                    c = piles[i] + max( stone(piles,i,j-1) , stone(piles,i+1,j) )
                return c
            
        Alex = stone(piles,0,len(piles)-1)
        s = sum(piles)
        Lee = s-Alex
        return Alex>Lee
