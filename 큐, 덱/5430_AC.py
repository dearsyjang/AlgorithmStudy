from collections import deque

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    func = input()
    N = int(input()) # 수의 개수
    arr = input()[1:-1].split(',')
    queue = deque(arr)
    reverse = False
    error = False

    if N == 0:
        queue = deque()
    for i in func:
        if i == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True

        elif i == 'D':
            if not queue:
                error = True
            else:
                if reverse == True:
                    queue.pop()
                else:
                    queue.popleft()

    if error == True:
        print('error')
    else:
        if reverse == True:
            queue.reverse()
            print('[' + ','.join(queue) + ']')
        else:
            print('[' + ','.join(queue) + ']')


