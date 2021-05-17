def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        def sol(small,big,req):
            i=0
            j=0
            while(i<len(big) and j<len(small)):
                dif = big[i]-small[j]
                if(dif==req):
                    return [small[j],big[i]]
                elif(dif>req):
                    j+=1
                else:
                    i+=1
                    
        aliceSizes.sort()
        bobSizes.sort()
        s1 = sum(aliceSizes)
        s2 = sum(bobSizes)
        req = (s1-s2)//2 if s1>s2 else (s2-s1)//2
        if(s1>s2):
            out = sol(bobSizes,aliceSizes,req)
            out[0],out[1]=out[1],out[0]
            return out
        else:
            out = sol(aliceSizes,bobSizes,req)
            return out
