class TimeMap:

    def __init__(self):
        self.mapdict = {}
        self.mapdict_l = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.mapdict.get(key, None) is None:
            self.mapdict[key] = []
            self.mapdict_l[key] = 0
        self.mapdict[key].append((timestamp, value))
        self.mapdict_l[key] += 1



    def get(self, key: str, timestamp: int) -> str:
        if self.mapdict_l.get(key, None) is None:
            return ""
        p, q = 0, self.mapdict_l[key]-1
        values = self.mapdict[key]
        result_time = -1
        result = ""
        while p <= q:
            mid = (p+q)//2
            if values[mid][0] == timestamp:
                result= values[mid][1]
                break
            elif values[mid][0] < timestamp:
                if values[mid][0] > result_time:
                    result = values[mid][1]
                    result_time = values[mid][0]
                # result = max(result, values[mid][0])
                p = mid+1
            else:
                q = mid - 1
        if result == -1:
            result = ""
        return result
