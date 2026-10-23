class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            else:
                if temp > stack[-1][0]:
                    # count = 1
                    while stack and temp > stack[-1][0]:
                        t, ix = stack.pop()
                        ans[ix] = i - ix
                
                stack.append((temp, i))
        while stack:
            t, ix = stack.pop()
            ans[ix] = 0
        return ans
                

        