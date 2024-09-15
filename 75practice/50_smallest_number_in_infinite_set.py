import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.set = set()
        self.min_num = 1

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.set.remove(num)
            return num
        else:
            self.min_num += 1
            return self.min_num - 1

    def addBack(self, num: int) -> None:
        if num not in self.set and self.min_num > num:
            heapq.heappush(self.heap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
