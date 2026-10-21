class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.min_ele: int|None = None
        self.top_ix: int = -1
        # print(f"initialized")

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_ix += 1
        if self.min_ele is None:
            self.min_ele = val
        elif val < self.min_ele:
            self.min_ele = val
        # print("pusshed ele")

    def pop(self) -> None:
        if not self.stack:
            return
        ele = self.stack.pop()
        self.top_ix -= 1
        if ele == self.min_ele and self.stack:
            self.min_ele = min(self.stack)
        if not self.stack:
            self.min_ele = None
        # print(f"pop ele {ele}")

    def top(self) -> int:
        # print("returning top ele")
        # print(f"{self.stack=}")
        if self.stack:

            return self.stack[self.top_ix]
        else:
            return -1

    def getMin(self) -> int:
        # print(f"returning min: {self.min_ele}")
        return self.min_ele