class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = dict(t)
        for c in t:
            check[c] = check.get(c,0)+1

        have, need = 0, len(check)

        left = 0
        resTuple = (0, 0)
        shortest = 0
        windowDict = dict()

        for i in range(len(s)):
            if s[i] in check:
                windowDict[s[i]] = windowDict.get(s[i], 0) + 1
                if windowDict[s[i]] == check[s[i]]:
                    have += 1


            while have == need:

                if i-left+1 < shortest:
                    shortest = i-left+1
                    resTuple = (left, i)

                if s[left] in check:
                    windowDict[s[left]] -= 1
                    if windowDict[s[left]] <check[s[left]]:
                        have -=1
                
                left+=1
        if shortest == 0:
            return ""
        return s[resTuple[0]:resTuple[1]+1]