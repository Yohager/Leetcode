class CQueue:

    def __init__(self):
        self.queue = []


    def appendTail(self, value: int) -> None:
        self.queue.append(value)


    def deleteHead(self) -> int:
        if self.queue == []: return -1
        else:
            pop_elem = self.queue[0]
            self.queue.pop(0)
            return pop_elem



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()