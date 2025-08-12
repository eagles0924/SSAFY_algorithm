import sys
sys.stdin = open('12396.txt', 'r')

"""
pop 할 때 대괄호 중괄호 소괄호  
"""

# def my_push(stack, item, size):
#     global top

T = int(input())
for tc in range(1, T+1):
    test = input()
    checklist = []      # 개형 괄호를 담기 위한 리스트 생성
    for word in test:
        if word in ['(', '{']:      # 개형 괄호이면 리스트에 추가
            checklist.append(word)
        elif word in [')', '}']:    # 폐형 괄호이면
            if len(checklist) == 0: # 그런데 폐형 괄호가 제일 먼저 위치하는 경우 바로 break
                break
            if word == ')' and checklist[-1] == '(':    #
                checklist.pop()
            elif word == '}' and checklist[-1] == '{':  # 괄호의 형태가 맞으면 pop
                checklist.pop()
            else:                                       # 형태가 맞지 않으면 break
                break
    if len(checklist) != 0:
        print(f"#{tc}", 0)
    elif len(checklist) == 0 and word in [')', '}']:
        print(f"#{tc}", 0)
    else:
        print(f"#{tc}", 1)