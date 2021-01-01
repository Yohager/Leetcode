class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []


    def push(self, x: int) -> None:
        self.minstack.append(x)


    def pop(self) -> None:
        self.minstack.pop(-1)


    def top(self) -> int:
        return self.minstack[-1]


    def min(self) -> int:
        return min(self.minstack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()