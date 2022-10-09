# ----------------------------시간 초과--------------------------
# T = int(input())
# queue = []
#
# for tc in range(1, T+1):
#     arr = input().split()
#     order = arr[0]
#
#     # push X: 정수 X를 큐에 넣기
#     if order == 'push':
#         X = int(arr[1])
#         queue.append(X)
#
#     elif order == 'pop':
#         # 큐에 정수가 없다면
#         if len(queue) == 0:
#             print(-1)
#         # 가장 앞에 있는 정수
#         else:
#             print(queue.pop(0))
#
#     elif order == 'size':
#         print(len(queue))
#
#     elif order == 'empty':
#         # 큐가 비어있으면
#         if len(queue) == 0:
#             print(1)
#         # 큐가 비어있지 않으면
#         else:
#             print(0)
#
#     elif order == 'front':
#         # 큐가 비어있으면
#         if len(queue) == 0:
#             print(-1)
#         # 큐가 비어있지 않으면, 가장 앞에 있는 정수
#         else:
#             print(queue[0])
#
#     elif order == 'back':
#         # 큐가 비어있으면
#         if len(queue) == 0:
#             print(-1)
#         # 큐가 비어있지 않으면, 가장 뒤에 있는 정수
#         else:
#             print(queue[-1])

import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
queue = deque([])

for tc in range(1, T+1):
    arr = input().split()
    order = arr[0]

    # push X: 정수 X를 큐에 넣기
    if order == 'push':
        X = int(arr[1])
        queue.append(X)

    elif order == 'pop':
        # 큐에 정수가 없다면
        if not queue:
            print(-1)
        # 가장 앞에 있는 정수
        else:
            print(queue.popleft())

    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        # 큐가 비어있으면
        if not queue:
            print(1)
        # 큐가 비어있지 않으면
        else:
            print(0)

    elif order == 'front':
        # 큐가 비어있으면
        if not queue:
            print(-1)
        # 큐가 비어있지 않으면, 가장 앞에 있는 정수
        else:
            print(queue[0])

    elif order == 'back':
        # 큐가 비어있으면
        if not queue:
            print(-1)
        # 큐가 비어있지 않으면, 가장 뒤에 있는 정수
        else:
            print(queue[-1])
        # 수정수정수정

