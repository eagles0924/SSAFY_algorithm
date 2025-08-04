# Array (배열)

'''
append()의 경우, 작은 list의 경우에는 괜찮지만 큰 list의 경우에는 연산 시간이 많이 소요된다.
추가하는 것이 아니라, 필요한 크기만한 배열을 만들고, 기존 내용의 복사 및 새로운 내용의 추가하는 연산 시간까지 소요된다.
for만 사용하기보다 while 문을 사용해주는 것이 좋다. (for ~ else도 사용)
list에는 자료형, 메모리 위치 등도 함께 저장되어있음.

알고리즘 문제에서 정수, 양수 등 제약 조건은 파이썬에서는 크게 의미 없고, 자료형을 선언해줘야 하는 다른 언어들에서 필요한 것.
값을 입력 받는 경우, 여러 빈칸도 처리하기 위해 split()을 실행.
'''

# 최댓값 or 인덱스 찾기

arr = list()
N = len(arr)
max_idx = 0
for i in range(1, N):
    if arr[max_idx] < arr[i]:       # 가장 앞에 있는 index 반환
        max_idx = i
        
for i in range(1, N):
    if arr[max_idx] <= arr[i]:      # 가장 나중의 index 반환
        max_idx = i

arr_idx = -1        # index가 없다고 가정


# 버블 정렬 (이중 for문 문법 연습)
'''
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
'''


# 그림 + 수도코드 사용

# 반드시 풀어야 할 문제 - min-max, 구간합, view
# 내장함수, 슬라이싱 쓰지 말기

