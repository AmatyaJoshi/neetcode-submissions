class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1+n2)
            elif i == "-":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1-n2)
            elif i == "*":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1*n2)
            elif i == "/":
                n2 = stack.pop()
                n1 = stack.pop()

                sign = -1 if (n1 < 0) != (n2 < 0) else 1
                stack.append(sign * (abs(n1) // abs(n2)))
            else:
                stack.append(int(i))
        return stack.pop()