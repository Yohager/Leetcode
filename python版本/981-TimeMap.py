class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d1 = collections.defaultdict(list)
        self.d2 = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d1[key].append(value)
        self.d2[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        tmp1 = self.d1[key]
        tmp2 = self.d2[key]
        #print(tmp1,tmp2)
        if not tmp1 and not tmp2:
            return ''
        if timestamp < tmp2[0]:
            return ''
        else:
            ans = bisect.bisect(tmp2,timestamp)
            return tmp1[ans-1]



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)