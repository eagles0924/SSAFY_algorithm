# 5명 중 3명 순서없이 고르기

arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []

def recur(cnt, start):
    # 종료조건: N명 뽑으면 종료
    if cnt == N:
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt+1, i+1)   # i번째 골랐으니 다음 선택은 i+1부터 고려
        # recur(cnt+1, i) # i면 뭐가 되는지??
        path.pop()

