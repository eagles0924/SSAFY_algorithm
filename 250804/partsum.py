# 시작과 끝, 시작과 길이
test_case = int(input())

for t in range(1, test_case+1):
    N, M = map(int, input().split())
    ex_list = list(map(int, input().split()))
    for i in range(N-M+1):
        ex_sum = 0
        for j in range(M):
            ex_sum += ex_list[i+j]
            if i == 0:
                max_sum, min_sum = ex_sum, ex_sum
        if ex_sum > max_sum:
            max_sum = ex_sum
        if ex_sum < min_sum:
            min_sum = ex_sum
    print(f"#{t} {max_sum - min_sum}")

'''
sm = sum(lst[:M])
mx = mn = sm

for j in range(1, N-M+1):
    sm = sm - lst[j-1] + lst[j+M-1]
'''

# 최적화 문제: 문제의 조건에 해당하는 값이 최대 혹은 최소인 경우를 찾는 문제
# 최대/최소인 경우를 최적해라고 한다.

# 
max_hap = 0     # 모든 원소가 양수이므로 음수는 나올 수가 없다.
min_hap = 1e6   # 하나의 원소 최댓값이 10,000이므로



for s in range(0, N-M+1):
    hap = 0
    for i in range(s, s+M):
            hap = lst[i]        # lst는 문제에서 주어짐.
    
    if max_hap < hap:
        hap = max_hap

# 그림을 그려서 인덱스를 계산??
# hap = 0
# for i in range(M):
#     hap += lst[i]
# max_hap = min_hap = hap

# for e in range(M, N):
#     i = e - M   # 빼줄 인덱스
#     hap += lst[e] - lst[i]

#     if max_hap < hap:
#         max_hap = hap