import sys
sys.stdin = open('12399.txt', 'r')

"""
stack을 어떻게 이용?
"""

def my_push():
    pass
def my_pop():


T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = []
    for char in s:
        if len(stack) != 0 and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    print(f"#{tc} {len(stack)}")