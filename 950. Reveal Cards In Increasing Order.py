def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        arr = []
        deck.sort()
        while(n>0):
            n-=1
            if(len(arr)>1):
                temp = arr.pop(-1)  # inserting last card on top
                arr.insert(0,temp)
            arr.insert(0,deck[n]) # inserting selected card on top
            
        return arr
