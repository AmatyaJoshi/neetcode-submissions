class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" or i == "}" or i == "]":
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
        
        return (False if stack else True)