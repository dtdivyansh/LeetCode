def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i = 0
            l = len(row)-1
            while(i<l):
                temp = 1-row[i]
                row[i] = 1-row[l]
                row[l] = temp
                l-=1
                i+=1
            if(i==l):
                row[i]=1-row[i]
        return image
