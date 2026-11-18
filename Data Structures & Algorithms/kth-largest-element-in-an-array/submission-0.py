class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = [nums[0]]
        heapq.heapify(h)
        l = len(nums)
        count = 1
        i = 1
        
        for i in range(1, l):
            heapq.heappush(h, nums[i])
            count += 1
            if count > k:
                heapq.heappop(h)
        return heapq.heappop(h)
        