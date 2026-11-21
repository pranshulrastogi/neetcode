class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        l = len(nums)
        def sub(i, ans):
            if i >= l:
                self.result.append(ans)
                return
            # take it
            sub(i+1, ans+[nums[i]])
            # leave it
            sub(i+1, ans)
            return
        sub(0, [])
        return self.result

        