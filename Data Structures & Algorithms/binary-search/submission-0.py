class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        p, q = 0, l-1
        while p <= q:
            mid = (p+q)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                q = mid-1
            else:
                p = mid+1
        return -1
        