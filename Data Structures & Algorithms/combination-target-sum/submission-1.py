class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        

        def get_comb(arr, target, curr_ans):
            if target == 0:
                result.append(curr_ans)
                return
            elif target < 0:
                return
            elif not arr:
                return
            else:
                for i, ele in enumerate(arr):
                    if ele > target:
                        break
                    get_comb(arr[i:], target-ele, curr_ans + [ele])
        nums.sort()
        get_comb(nums, target, [])
        # print(result)
        return result