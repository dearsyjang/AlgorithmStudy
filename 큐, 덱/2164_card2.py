import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque([])

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue[-1])