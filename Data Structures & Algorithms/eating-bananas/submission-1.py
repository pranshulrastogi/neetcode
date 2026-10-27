class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        l = len(piles)
        if h == l:
            return mx
        p, q = 1, mx
        ans = None

        def get_hours(mid):
            # lst = []
            result = 0
            for val in piles:
                if val <= mid:
                    result += 1
                    # print(f"{val=} result + 1")
                else:
                    result += (val//mid)
                    # print(f"{val=} result + val//mid + 1")
                    if val % mid:
                        result += 1
            return result 

            # result = sum([(val)//mid for val in piles])
            # return result

        while p <= q:
            mid = (p+q)//2
            print(f"{mid=}")
            hours = get_hours(mid)
            print(f"{hours=}")
            if hours > h:
                p = mid + 1
                # if ans is not None:
                #     break
            elif hours <= h:
                if ans is None:
                    ans = mid
                else:
                    ans = min(ans, mid)
                print(f"{ans=}, {hours=}")
                q = mid - 1
        print(ans)
        return ans