# A, J, Q, K가 넉넉하게 있다.
# 카드 5장 뽑았을 때 같은 종류의 카드가 3장 연속으로 나오는 경우의 수

cards = ['A', 'J', 'Q', 'K']
path = []

def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False    # 일단 false를 return 하도록 만듦.

result = 0
def recur(cnt):
    global result

    if cnt == 5:
        # Todo: 연속된 3개가 나오면 counting
        if count_three():
            result += 1
            print(*path)
        return

    # 카드 중 하나 선택
    for idx in range(len(cards)):
        path.append(cards[idx])
        recur(cnt + 1)
        path.pop()

recur(0)
print(result)


# baby jin 재귀로 구현해보기 #

