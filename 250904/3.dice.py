# 주사위 3개를 던져 합이 10이하인 케이스

path = []
result = 0
def recur(cnt):
    global result

    # 합이 10을 초과하는 경우는 볼 필요 없다.
    # 기저 조건에서 많은 경우의 수를 줄일 수 있다.
    if sum(path) > 10:
        return

    if cnt == 3:
        if sum(path) <= 10:
            result += 1
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()
print(recur(0), result)

# 그렇다면 굳이 path에 모두 저장을 해야할까? 출력만 하면 되는데?

# 누적합을 활용하는 버전

def recur(cnt, total):
    global result

    if total > 10:
        return

    if cnt == 3:
        result += 1
        return

    for num in range(1, 7):
        recur(cnt + 1, total + num)

# sum(path)를 total로 줄여 연산 시간을 줄일 수 있다.
# 누적합의 경우 저장보다는 파라미터에 값만 넘겨주는 것이 좋다.

