import sys
input = sys.stdin.readline

T = int(input())
stack = []
# result = 0

for tc in range(1, T+1):
    arr = input().split()
    order = arr[0]

    # push X: 정수 X를 스택에 넣기
    if order == 'push':
        X = int(arr[1])
        stack.append(X)

    # pop: 가장 위에 있는 정수 출력, 정수가 없는 경우 -1
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) # 출력하고 pop!!
            stack.pop()

    # size: 스택에 들어있는 정수의 개수 출력
    elif order == 'size':
        print(len(stack))

    # empty: 스택에 비어있으면 1, 아니면 0 출력
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # 스택의 가장 위에 있는 정수 출력, 없을 경우 -1 출력
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
