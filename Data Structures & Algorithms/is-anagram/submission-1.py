class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = {}
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            words[s[i]] = words.get(s[i], 0)+1
            words[t[i]] = words.get(t[i], 0)-1
        return all(value ==0 for value in words.values())

