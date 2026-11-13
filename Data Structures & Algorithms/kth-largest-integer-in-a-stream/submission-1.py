class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort()
        self.k = k
        self.l = len(nums)
        self.ix = self.l-self.k
        # print(f"{self.ix=}")
        

    def add(self, val: int) -> int:
        # print(f"add {val}")
        
        if self.ix >= 0 and val < self.nums[self.ix]:
            # print(f"returning old")
            return self.nums[self.ix]
        self.nums.append(val)
        self.l += 1
        i = self.l-2
        while i >= self.ix:
            if self.nums[i] > val:
                self.nums[i+1] = self.nums[i]
                i -= 1
            else:
                self.nums[i+1] = val
                # self.nums[i+1] = self.nums[i]
                # self.nums[i] = val
                break
        self.ix += 1
        # print(f"new arr: {self.nums=}, {self.ix=}")
        return self.nums[self.ix]

