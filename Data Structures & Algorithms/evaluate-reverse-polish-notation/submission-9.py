import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack  = []
        valid_symbols = ["+", "-","*","/"]
        for token in tokens:
            if token not in valid_symbols:
                numStack.append(int(token))
            else:
                if len(numStack) >=2:
                    if token == '+':
                        numStack[-2] = numStack[-1] + numStack[-2]
                    elif token == '*':
                        numStack[-2] = numStack[-1] * numStack[-2]
                    elif token == '-':
                        numStack[-2] = numStack[-2] - numStack[-1]
                    elif token == '/':
                        numStack[-2] = int(numStack[-2] / numStack[-1])

                    del numStack[-1]
            print(numStack)
        return numStack[0]
                        