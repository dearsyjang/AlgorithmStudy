import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
position = list(map(int, input().split()))
queue = deque([])

for i in range(1, len()):
    queue.append(i)

cnt = 0
for i in position:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            # 뒤쪽이 가까움. appendleft() => 왼쪽으로 옮기자!
            if queue.index(i) > len(queue)//2:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1
            # 앞쪽이 가까움. append() => 오른쪽으로 옮기자!
            elif queue.index(i) <= len(queue):
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1

print(cnt)

