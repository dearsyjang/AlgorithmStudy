import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
queue = deque()

for tc in range(1, T+1):
    arr = list(input().split())
    order = arr[0]

    # push_front X: 정수 X를 덱 앞에 넣기
    if order == 'push_front':
        X = int(arr[1])
        queue.appendleft(X)

    # push_back X: 정수 X를 덱 뒤에 넣기
    elif order == 'push_back':
        X = int(arr[1])
        queue.append(X)

    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 만역 없는 경우 -1
    elif order == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 만약 없는 경우 -1
    elif order == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)

    # size: 정수의 개수
    elif order == 'size':
        print(len(queue))

    # empty: 덱이 비어있으면 1, 아니면 0
    elif order == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    # front: 가장 앞에 있는 정수 출력
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    #back: 가장 뒤에 있는 정수 출력
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)



