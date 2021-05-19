def largestAltitude(self, gain: List[int]) -> int:
        s = alt = 0
        for i in gain:
            s+=i
            if(s > alt):
                alt = s
        return alt
