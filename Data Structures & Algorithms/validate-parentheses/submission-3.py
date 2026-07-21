class Solution:
    def isValid(self, s: str) -> bool:
        sample_dict = {')': '(', '}':'{',']':'['}
        stack = []

        for i in s:
            if i in sample_dict:
                temp = stack.pop()
                if temp != sample_dict[i]:
                    return False
            else:
                stack.append(i)
        return True