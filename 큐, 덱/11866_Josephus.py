import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())
queue = deque([])
result = []

for i in range(1, N+1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue[0])
        queue.popleft()
    result.append(queue.popleft())

print('<', end='')
for i in range(len(result)-1):
    print(f'{result[i]}, ', end='')
print(result[-1], end='')
print('>', end='')
