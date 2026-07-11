class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        for n in range(len(min(strs, key = len))):
            current_char = strs[0][n]
            counter = 0
            for words in strs:
                if words[n] == current_char:
                    counter+=1
            if counter == len(strs):
                longest+=current_char
            else:
                return longest
        return longest
        