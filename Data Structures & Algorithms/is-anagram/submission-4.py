class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        sampleDict = [0] * 26
        for i in range(len(s)):
            sampleDict[ord(s[i])-ord('a')] +=1
            sampleDict[ord(t[i])-ord('a')] -=1
        
        return len(set(sampleDict)) == 1
        
