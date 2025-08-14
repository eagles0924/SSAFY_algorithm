import sys
sys.stdin = open('11613.txt', 'r')

"""
1. 연산자와 연산자가 아닌 것 (숫자)로 구분하기
2. 숫자이면 stack_num에 받고, 연산자이면 stack_num에서 pop() 두 번 하여 연산자와 계산
"""

# top 이용해서 index로 풀기

# T = int(input())
# for tc in range(1, T+1):
#     ex = input().split()
#     stack_num = [[] for _ in range(len(ex))]
#     top = -1
#     calculator = ['+', '-', '*', '/']
#     for i in ex:
#         if i not in calculator:     # 숫자일 때
#             top += 1
#             stack_num[top] = i  # 연산자일 때
#         elif i in calculator:
#             b = stack_num.pop(top); top -= 1
#             a = stack_num.pop(top); top -= 1
#             if i == '+':
#                 top += 1; stack_num[top] = int(a) + int(b)
#             elif i == '-':
#                 top += 1; stack_num[top] = a - b
#             elif i == '*':
#                 top += 1; stack_num[top] = a + b
#             elif i == '/':
#                 top += 1; stack_num[top] = a + b
#         elif i == '.':
#             break
#     print(f"#{tc} {stack_num.pop()}")

"""
오류
1. 연산자가 먼저 들어오는 경우
2. 연산자가 마지막에 남는 경우
3. 

"""

T = int(input())
for tc in range(1, T+1):
    ex = input().split()
    stack = []; err = 0
    # 먼저 숫자 개수 -1 = 연산자 개수 부터 확인
    num_cal, num_num = 0, 0
    for i in ex:
        if i in '+-*/':
            num_cal += 1
    num_num = len(ex) - num_cal
    if num_num - num_cal != 2:
        err += 1

    for i in ex:
        if i == '.':                # 종료하면
            break
        elif i not in '+-*/':       # 숫자일 때
            stack.append(i)
        elif i in '+-*/':           # 연산자일 때
            if stack:               # 정수 하나 뺄 수 있으면
                b = int(stack.pop())
                if stack:           # 정수 하나 더 뺄 수 있으면 연산
                    a = int(stack.pop())
                    if i == '+':
                        stack.append(a + b)
                    elif i == '-':
                        stack.append(a - b)
                    elif i == '*':
                        stack.append(a * b)
                    elif i == '/':
                        stack.append(a // b)
                elif not stack:     # stack 안에 정수 하나밖에 없는 경우
                    err += 1
                    break
            elif not stack:         # stack 안에 정수가 아예 없는 경우 에러문 출력 후 break
                err += 1
                break
    if err == 0:
        print(f"#{tc} {stack.pop()}")
    else:
        print(f"#{tc} error")

# T = int(input())
# for tc in range(1, T+1):
#     ex = input().split()
#     stack_num = []
#     # 먼저 숫자 개수 -1 = 연산자 개수 부터 확인
#     num_cal, num_num = 0, 0
#     for i in ex:
#         if ex in '+-*/':
#             num_cal += 1
#     num_num = len(ex) - num_cal
#     if num_num - num_cal != 1:
#         print(f"#{tc} error")
#         break
