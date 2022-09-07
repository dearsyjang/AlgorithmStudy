import sys
input = sys.stdin.readline

from collections import deque

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    func = sys.stdin.readline().strip()
    N = int(sys.stdin.readline()) # 수의 개수
    arr = map(int, sys.stdin.readline().strip()[1:-2].split(','))
    queue = deque(arr)
    reverse = False

    if N == 0:
        print('error')
        break
    else:
        for i in func:
            if i == 'R':
                if reverse == False:
                    reverse = True
                else:
                    reverse = False

            elif i == 'D':
                if not queue:
                    print('error')
                    break
                else:
                    if reverse == True:
                        queue.pop()
                    else:
                        queue.popleft()

    if not queue:
        print('error')
    elif queue:
        if reverse == True:
            queue.reverse()
            print([*queue])
        else:
            print([*queue])




