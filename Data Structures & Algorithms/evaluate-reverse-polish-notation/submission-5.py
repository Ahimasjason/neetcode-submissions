class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        ops = {
                    
                        "+" : lambda x, y: x + y,
                         "-": lambda x, y: x - y,
                        "*": lambda x, y:  x * y,
                        "/": lambda x, y:  int(x / y)
                    
        }
        for tok in tokens:
            if tok in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[tok](b, a))
            else:
                stack.append(int(tok))


        return stack.pop()