import sys
input = sys.stdin.readline

T = int(input())
stack = []

for tc in range(1, T+1):
    money = int(input())

    # 0이 아닐 경우, 장부에 추가 (push)
    if money != 0:
        stack.append(money)

    # 0일 때, 최근에 쓴 수, 지우기 (pop)
    else:
        stack.pop()

result = sum(stack)
print(result)
