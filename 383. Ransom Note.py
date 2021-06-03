def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = [i for i in ransomNote]
        mag = [i for i in magazine]
        for i in ran:
            if(i in mag):
                mag.remove(i)
            else:
                return False
        return True
