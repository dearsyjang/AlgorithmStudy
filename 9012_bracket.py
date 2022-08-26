import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    stack = []
    data = input()
    isVPS = True

    for i in data:
        # 여는 괄호 push
        if i == '(':
            stack.append(i)

        # 닫는 괄호 pop
        elif i == ')':
            # 만약 stack이 비었다면?
            if not stack:
                isVPS = False
                break
            # stack에 여는 괄호가 있다면 pop
            else:
                stack.pop()

    if not stack and isVPS == True:
        print('YES')
    elif stack:
        print('NO')
    elif isVPS == False:
        print('NO')




