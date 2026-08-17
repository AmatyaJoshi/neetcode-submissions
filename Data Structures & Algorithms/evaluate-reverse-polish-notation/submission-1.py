class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandSet = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operandSet:
                stack.append(int(token))
                continue
            secondOperand = stack.pop()
            firstOperand = stack.pop()
            result = 0
            match token:
                case "+":
                    result = firstOperand + secondOperand
                case "-":
                    result = firstOperand - secondOperand
                case "*":
                    result = firstOperand * secondOperand
                case "/":
                    result = abs(firstOperand) // abs(secondOperand)
                    if (firstOperand < 0 and secondOperand > 0) or (firstOperand > 0 and secondOperand < 0):
                        result *= -1
            stack.append(result)

        return stack[0]
            