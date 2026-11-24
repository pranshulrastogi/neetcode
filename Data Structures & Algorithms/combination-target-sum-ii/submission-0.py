class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def comb(arr, curr_ans, target):
            if target == 0:
                result.append(curr_ans)
                return
            elif target < 0:
                return
            else:
                prev = 0
                l = len(arr)
                for i, ele in enumerate(arr):
                    if ele > target:
                        break
                    if ele != prev:
                        if i < l-1:
                            comb(arr[i+1:], curr_ans + [ele], target-ele)
                        else:
                            if ele == target:
                                result.append(curr_ans + [ele])
                    prev = ele
                return
        
        comb(candidates, [], target)
        return result
        