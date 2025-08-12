# ########### STACK - (1)

# # top을 index로 사용
 
# class my_stack:
#     def __init__(self, stack):
#         self.stack = stack

#     def isempty(self):
#         pass

#     def my_push(self, item, size):
#         global top
#         top += 1
#         if top == size:
#             print('!overflow!')
#         else:
#             self.stack[top] = item
    
#     def my_pop(self):
#         if len(self.stack) == 0:
#             # underflow
#             return
#         else:
#             return self.stack.pop()

# ######
# stack = []

# def my_pop():
#     global top
#     if top == -1:
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top+1]
# print(pop())

# # while stack:    stack에 아무 요소도 없으면 실행되지 않음.

# # 연습문제 1: 1, 2, 3 순서대로 push 후 pop

# stack = []
# def my_push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('overflow')
#     else:
#         stack[top] = item
# my_push()

# #######
# # 10칸짜리 stack임을 가정

# top = -1
# stack = [0]*10

# top += 1
# stack[top] = 1
# top += 1
# stack [top] = 2
# top += 1
# stack[top] = 3


# ########## 응용
# # 괄호 검사

# txt = input()
# top = -1
# stack = [0]*100

# for x in txt:
#     if x == '(':
#         top += 1
#         stack[top] = x      # stack.append()
#     elif x == ')':
#         if top == -1:
#             ans = 0
#             break
#     else:
#         top -= 1

# ############
# stack [0]*100
# top = -1
# for x in txt:
#     if x in ['(', '{', '[']:
#         top += 1
#         stack[top] = x
#     elif x in [')', '}', ']']:
#         if top == -1:
#             ans = 0
#             break
#         else:
#             top = -1


######### 강사님

# N = 5
# S = [0]*N
# top = -1
#
# def push(item):
#     global top
#     # overflow check
#     if top == N-1:
#         return
#     top += 1
#     S[top] = item
#
# def my_pop():
#     global top
#     # underflow
#     if top == -1:
#         return
#     ret = S[top]
#     top -= 1
#     return ret
#
# for val in range(5):
#     push(val)
#
# while S:
#     print(S.pop())

## flag 체크포인트
## flag = True로 놓고, 특정 구간에서 flag = False로 검사
word = 'sometimes'
N = len(word)
word_list = [w for w in word]
for i in range(N//2):
    word_list[i], word_list[N-i-1] = word_list[N-i-1], word_list[i]
print(''.join(word_list))

def solution(s):
    stack = []

    for char in s:
        if len(stack) > 0 and stack[-1] == char:        # stack에 문자가 차있고,
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))


### 연습문제 2

txt = input()

top = -1
stack = [None]*100

for x in txt:
    if x == '(':
        top += 1
        stack[top] = x
    elif x == ')':
        if top == -1:
            ans = 0
            break
        if check == '(':















