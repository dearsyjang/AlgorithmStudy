# 테스트케이스 수를 정확하게 모르니까 값이 있다면, 계속
while True:
    data = input()
    stack = []

    # 각 줄은 마침표(.)로 끝난다
    if data == '.':
        break

    for i in data:
        # 여는 괄호 stack에 push
        # if i == '(' or '[': => 이렇게 하면 모든 글자들이 다 push된다 왜?
        if i == '(' or i == '[':
            stack.append(i)

        # 닫는 괄호 stack에 pop
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    if stack:
        print('no')
    elif not stack:
        print('yes')
