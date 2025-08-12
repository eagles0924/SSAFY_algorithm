### stack에 push 하는 법

# 1
s = []  # 사용할 stack 선언
def my_push(item):
    s.append(item)  # append를 사용하여 stack에 원소를 추가하는 법
# 2

N = 100     # stack의 크기 설정 (초기 설정 후에 변경할 수 없기 때문에 문제를 잘 읽거나 상황에 맞게 설정)
stack = [None]*N
top = -1    # stack의 최대 index를 나타내는 변수 top 초기화
def my_push(item, size):
    global stack, top
    top += 1    # index는 0부터 시작하기 때문
    if top == size:
        print('OVERFLOW')
    else:
        s[top] = item


### stack에 pop 하는 법

# 1
stack = [None]*100
def my_pop():
    global stack
    if len(s) == 0:
        print('UNDERFLOW')
        return
    else:
        return s.pop()


# 2
stack = [None]*100
def my_pop():
    global stack, top
    if len(s) == 0:
        return None
    else:
        top -= 1
        return