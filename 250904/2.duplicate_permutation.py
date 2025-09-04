

path = []

def recur(cnt):
    if cnt == 2:
        print(*path)
        return

    path.append(0)
    recur(cnt+1)

    path.append(1)
    recur(cnt+1)

    path.append(2)
    recur(cnt+1)

print(recur(0))

##########################

def recur(cnt):
    if cnt == 2:
        print(*path)
        return

    for num in range(3):
        path.append(num)
        recur(cnt+1)
        path.pop()
print(recur(0))

###########################
# 중복 제거 및 초기화 포함

used = [False] * 7
used = [0] * 7

def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    for num in range(1, 7):
        # 중복 제거
        if used[num]:
            continue

        used[num] = 1   # 아니면 True
        path.append(num)
        recur(cnt + 1)
        path.pop()
        used[num] = 0
recur(0)

