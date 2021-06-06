def compress(self, chars: List[str]) -> int:
        i=0
        while(i<len(chars)):
            c=1
            j=i+1
            while(j<len(chars)):
                if(chars[j]!=chars[i]):
                    break
                c+=1
                chars.pop(j)
            if(c!=1):
                new = str(c)
                l=len(new)
                for x in new:
                    chars.insert(i+1,x)
                    i=i+1
            i+=1
        return len(chars)
