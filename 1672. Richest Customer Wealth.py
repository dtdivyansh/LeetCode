def maximumWealth(self, accounts: List[List[int]]) -> int:
        final = 0
        for customer in accounts:
            if( sum(customer) > final ):
                final = sum(customer)
        return final
