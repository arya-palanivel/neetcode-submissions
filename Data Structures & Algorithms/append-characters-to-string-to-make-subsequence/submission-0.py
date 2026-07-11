class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sIndex = 0
        tIndex = 0
        while sIndex< len(s) and tIndex < len(t):
            if(s[sIndex] == t[tIndex]):
                tIndex +=1
            sIndex+=1
        
        if(tIndex != len(t)):
            return len(t)-tIndex
        else:
            return 0