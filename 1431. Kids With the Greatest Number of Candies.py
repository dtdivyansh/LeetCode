def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = max(candies)
        final = []
        for i in candies:
            final.append( i+extraCandies >= high )
        return final
