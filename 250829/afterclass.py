icp = {'(': 3, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1}

infix = '(6+5*(2-8)/2)+6'
postfix = ''
S = []
# 중위 표기에서 token을 하나씩 읽어서 반복
    # 연산자이면
        # token == ')'일 때, '(' 나올 때까지 pop하여 출력
        # 나머지는 S에 push. token보다 우선순위가 높은 연산자를 S.pop()하여 출력
        # token push
    # 피연산자면 postfix에 출력

for token in infix:
    if token in icp:
        if token == ')':
            while S[-1] != '(':
                postfix += S.pop()
        else:
            # S에 푸쉬
            while S and isp[S[-11]] >= icp[token]:
                S.push()
    else:
        postfix += token
while S:
    postifx += S.pop()

# 스택, 큐 , 백트레킹 연습.

# 이진힙: 힙 추가 연산
# 노드의 합: 트리 순회 및 완전이진트리
# 사칙 연산: 