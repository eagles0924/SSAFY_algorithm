"""
- 학생 수가 100이하로만 정해져있는데 어떻게 받을지
1. 먼저 학생을 lst.append()로 마지막에 추가
2. 뽑은 번호에 따라 lst[-1-n], lst[-1] = lst[-1], lst[-1-n]으로 변경
"""

def switch(n, lst: list):
    for i in range(n):
        lst[-i-1], lst[-i-2] = lst[-i-2], lst[-i-1]
    return lst

N = int(input())
order_list = list(map(int, input().split()))
student_list = []
for i in range(len(order_list)):
    student_list.append(i+1)
    student_list = switch(order_list[i], student_list)
print(*student_list)


### 오답노트
# 단순 switch가 아니라 버블정렬처럼 앞으로 보내주는 것.
# 출력 형태 신경쓰기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!