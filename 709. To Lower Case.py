def toLowerCase(self, str: str) -> str:
        res = ''
        for i in str:
            if( i.isupper() ):
                res=''.join([res,i.lower()])
            else:
                res=''.join([res,i])
        return res
        
