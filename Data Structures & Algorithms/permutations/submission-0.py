class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result = []
        
        def perm(arr, curr):
            print(f"{arr=}, {curr=}")
            if len(curr) == l:
                result.append(curr)
                return
            if not arr:
                result.append(curr)
                return 
            for i, ele in enumerate(arr):
                left, right = [], []
                # if i >= 1:
                left = arr[:i]
                # if i < l-1:
                right = arr[i+1:]
                perm(left+right, curr+[ele])
            return
        
        perm(nums, [])
        return result
        