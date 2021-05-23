def numTeams(self, rating: List[int]) -> int:
        teams = 0
        n = len(rating)
        for sel in range(1,n-1):
            rightLess = rightMore = leftLess = leftMore = 0
            
            #For Left subarray
            for prev in range(sel-1,-1,-1):
                if( rating[prev] < rating[sel] ):
                    leftLess+=1
                else:
                    leftMore+=1
                    
            #For Right Subarray
            for nexT in range(sel+1,n):
                if( rating[nexT] < rating[sel] ):
                    rightLess+=1
                else:
                    rightMore+=1
                    
            #Concatenating total result
            teams+= leftLess*rightMore + leftMore*rightLess
            
            # leftLess*rightMore will give teams with sel in middle of ascending order
            # leftMore*RightLess will give teams with sel in middle of decending order
            
        return teams
