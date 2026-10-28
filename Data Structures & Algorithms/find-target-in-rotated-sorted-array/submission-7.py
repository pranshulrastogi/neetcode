class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        
        def find_cut():
            p, q = 0, l-1
            if p == q:
                return p
            while p <= q:
                mid = (p+q)//2
                if nums[mid-1] > nums[mid]:
                    return mid
                elif nums[mid-1] < nums[mid]:
                    if nums[mid] > nums[q]:
                        # go right
                        p = mid + 1
                    else:
                        q = mid - 1
        
        point = find_cut()
        # print(point)

        def bs(p, q):
            while p <= q:
                mid = (p+q)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    q = mid - 1
                else:
                    p = mid + 1
            return -1
        
        # if point == 0:

        res = bs(0, point-1)
        print(f"called bs(0, {point-1}), returned {res}")
        if res == -1:
            res = bs(point, l-1)
            print(f"called bs({point}, {l-1}), {res=}")
        return res