class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        maxlen = 0

        l,r = 0, 0
        while r<len(s):
            while(s[r] in count):
                maxlen = max(maxlen, len(count))
                count.remove(s[l])
                l+=1


            count.add(s[r])
            r+=1
        maxlen = max(maxlen, len(count))
        return maxlen