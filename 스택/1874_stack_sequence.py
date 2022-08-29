T = int(input())

stack = []
answer = []
num = 1
result = True

for tc in range(1, T+1):
    N = int(input())

    # N보다 작은 수 push
    while N >= num:
        stack.append(num)
        answer.append('+')
        num += 1

    # N만큼 왔을 때 pop
    if stack[-1] == N:
        stack.pop()
        answer.append('-')

    # 스택 수열을 만들 수 없다면 NO
    else:
        result = False

if result == True:
    for j in answer:
        print(j)
else:
    print('NO')