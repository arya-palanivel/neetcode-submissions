class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # checkDict = dict()
        # for i in t:
        #     dict
        have, need = 0, len(t) 
        left = 0
        restTuple = (0,0)
        longest = 0
        windowDict = dict()
        for i in range(len(s)):
            if (s[i] in check):
                windowDict[s[i]] = windowDict.get(s[i],0) + 1
                if (windowDict[s[i]]==1):
                    have +=1
            if have == need:
                done = False
                while True:
                    if (windowDict[s[left]]in check and windowDict[s[left]]==1):
                        have -=1
                        if(done):
                            have+=1
                            break
                        done = True
                    else:
                        left+=1
                        if(windowDict[s[left]] in check):
                            windowDict[s[left]]-=1
                resTuple = (left, i)
                longest = i-left +1
            
