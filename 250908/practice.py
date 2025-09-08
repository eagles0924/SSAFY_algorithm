# A ~ E 중 3명을 뽑을 수 있는 모든 경우

arr = ['A', 'B', 'C', 'D', 'E']
n = 3
path = []   # 뽑은 친구들 저장

def recur(cnt, start):
    # 종료 조건
    if cnt == 3:
        print(path)
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt+1, i+1)
        path.pop()
recur(0, 0)

# Fractional knapsack

n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)]

total = 0   # 총 가격
for kg, price in things:
    per_kg = price / kg
    
    if target < kg:
        total += target * per_kg
        target = 0
        break 
    target -= kg
    total += price
