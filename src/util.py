from collections import deque
import os

class VideoQueue:

    def __init__(self, size = 50):
        self.q = deque([])
        self.size = size

    def push(self, filename):
        self.q.append(filename)
        if len(self.q) > self.size:
            os.remove(self.q.popleft())

if __name__ == '__main__':
    q = VideoQueue(50)
    for i in range(51):
        q.push("filename"+str(i))
