class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {']':'[','}':'{',')':'('}
        for i in s:
            if i in myDict.values():
                stack.append(i)
            else:
                if len(stack) ==0 or stack.pop() != myDict[i] :
                    return False
        return True if len(stack) ==0 else False