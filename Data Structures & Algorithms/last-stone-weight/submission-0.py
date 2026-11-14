class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        s = [-1*val for val in stones]
        heapq.heapify(s)
        l = len(stones)
        while s and l > 1:
            m1, m2 = heapq.heappop(s), heapq.heappop(s)
            m1, m2 = -1*m1, -1*m2
            print(f"{m1=}, {m2=}")
            diff = abs(m1-m2)
            l -= 2
            if diff:
                heapq.heappush(s, -1*diff)
                print(f"pushed {diff}")
                l += 1
        if s:
            ans = -1*heapq.heappop(s)
        else:
            ans = 0
        return ans

        