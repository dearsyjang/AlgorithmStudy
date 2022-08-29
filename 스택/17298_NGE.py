import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
NGE = [-1] * N

stack.append(0)
# 인덱스를 stack으로 활용하기
for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        NGE[stack.pop()] = arr[i]
    stack.append(i)

# 리스트 풀기
print(*NGE)
