from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


obj = RecentCounter()
answer = obj.ping(t=1)
answer = obj.ping(t=100)
answer = obj.ping(t=3001)
answer = obj.ping(t=3002)
print("answer is")
print(answer)
