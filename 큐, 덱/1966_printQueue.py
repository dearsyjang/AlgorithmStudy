from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 문서의 개수, 몇 번째
    queue = deque(list(map(int, input().split()))) # 중요도
    idx_queue = deque([]) # 인덱스
    cnt = 0 # 순서

    for i in range(N):
        idx_queue.append(i)

    # 중요도 큐와 인덱스 큐를 똑같이 돌리자!
    while queue:
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()
            if idx_queue.popleft() == M:
                print(cnt)
        else:
            queue.append(queue.popleft())
            idx_queue.append(idx_queue.popleft())





