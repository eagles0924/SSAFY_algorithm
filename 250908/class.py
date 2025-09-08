"""
종료조건
후보 수
"""

# subset recursion
arr = ['O', 'X']
name = ['MIN', 'CO', 'TIM']
path = []

def recur(cnt):
    # 종료조건
    if cnt == 3:
        return
    
    # 후보군 (재귀호출 파트)
    # 부분집합에 포함 O (O 추가)
    path.append(arr[0]) # O를 선택했다고 가정하고
    recur(cnt+1)    # 다음 회차 선택 진행
    path.pop()

    # 부분집합 포함 X (X 추가)
    path.append(arr[1])
    recur(cnt+1)
    path.pop()
    pass



def recur2(cnt, subset):
    if cnt == 3:
        print(*subset)
        return
    
    # 부분집합에 새로 들어온 이름을 포함시키는 경우
    recur2(cnt+1, subset+[name[cnt]])

    # 포함시키지 않는 경우
    recur2(cnt+1, subset)

recur2(0, [])

a = []
print(id(a), id(a+[1]))

"""
arr = []
arr = arr + [1]     # 기존의 arr과 새로 생성된 arr의 메모리 주소 다르다.
arr += [1]          # 기존 arr과 새로 생성된 arr 메모리 주소 같음.
"""