class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def gen(n, o, c, curr):
            if n == 0 and o == c:
                result.append(curr)
            else:
                if n == 0:
                    # u can't open and only close it
                    gen(n, o, c+1, curr+")")
                else:
                    gen(n-1, o+1, c, curr+"(")
                    if o > c:
                        gen(n, o, c+1, curr+")")
        gen(n, 0, 0, "")
        return result

        