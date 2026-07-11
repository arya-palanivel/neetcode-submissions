class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
             return False

        sample = [0] * 26

        for letter in s: 
            sample[ord(letter)-ord('a')] +=1
        for letter in t:
            sample[ord(letter)-ord('a')] -=1
        if sample != [0] *26:
            return False
        return True