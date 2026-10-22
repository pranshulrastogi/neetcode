class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ["+", "-", "*", "/"]
        ans = 0
        for c in tokens:
            if c in operation:
                b, a = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(a+b)
                elif c == "-":
                    stack.append(a-b)
                elif c == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(c))
            # print(f"{c=} {stack=}")
        return stack[-1]
            

        