class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chrset = set()
        longest = 0
        left = 0
        for i in range(len(s)):
            while (s[i] in chrset):
                chrset.remove(s[left])
                left+=1
            chrset.add(s[i])
            longest = max(longest, len(chrset))
        return longest

