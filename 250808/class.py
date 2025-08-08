### 코드 체계

# bit 복수로 쓸 때는 7-bit 혹은 7bits와 같은 형식으로 작성하기. (7 bit 안된다.)
#
print('\ub364')

# Endian
## Big-endian / little-endian 두가지 방식이 있는데 최근에는 대부분 ??? 방식을 사용한다. (AM 09:36 경)


# 유니코드 인코딩(utf-8) 다시 보기
#



################### 11 ~

##### 선택 정렬

arr = [5, 3, 2, 6, 1, 4]
N = len(arr)

idx = 0
print(arr)
for i in range(N):
    idx = i
    for j in range(i+1, N):
        if arr[idx] > arr[j]:
            idx = j
    arr[i], arr[idx] = arr[idx], arr[i]
    print(arr)

##### 이진 탐색: 반드시 정렬 후에 사용해야 함.

arr = [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]
N = len(arr)

def binary_search(l, r, key):
    while l <= r:
        # 범위의 중간 위치 인덱스 계산
        mid = (l + r) // 2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1   # 탐색 실패 시

##### 달팽이 숫자:
N = 4
arr = [[0]*N for _ in range(N)]

dr , dc = [0, 1, 0, -1], [1, 0, -1, 0]
dir = 0 # 최초 방향
r, c = 0, -1
num = 1
while num <= N*N:
    nr, nc = r + dr[dir], c + dc[dir]
    # 변경된 위치가 실제로 도달할 수 있는 위치인지
    if ((nr < 0) or (nr >= N) or (nc < 0) or (nc >= N)) or arr[nr][nc] != 0:
        dir = (dir + 1) % 4     # 나머지 연산자를 사용해서 방향 반복해주기
    else:
        r, c = nr, nc
        arr[nr][nc] = num
        num += 1


# 문자열_글자수
# 문자열_회문_확인용
# [S/W 문제해결 기본] 5일차 - GNS