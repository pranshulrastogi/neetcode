class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        i = 0
        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            dist.append((d, i))
            # dist[i] = d
            i += 1
        import heapq
        heapq.heapify(dist)
        i = 0
        ans = []
        while i < k:
            val = heapq.heappop(dist)
            ans.append(points[val[1]])
            # ans.append(val)
            i += 1
        return ans

        

        