# N-Queen

# 순열 생성 적용

# \, / 생성 위해 길이 2N의 배열 생성

# 대각 두방향을 확인하는 것. 방법 다시 이해하기.

import heapq

arr = [20, 15, 19, 4, 13, 11]

min_heap = []
for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)

max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)
print(max_heap)

while max_heap:
    print(-heapq.heappop(max_heap), end=' ')
