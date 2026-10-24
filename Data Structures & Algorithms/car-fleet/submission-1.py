class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(position)
        pos_speed = zip(position, speed)
        pos_speed = sorted(pos_speed, reverse=True)
        stack = [(target-pos_speed[0][0])/pos_speed[0][1]]
        ans = 1
        for pos, s in pos_speed[1:]:
            time = (target-pos)/s
            if stack:
                if stack[-1] >= time:
                    continue
                else:
                    stack.append(time)
        ans = len(stack)
        print(ans)
        return ans
        