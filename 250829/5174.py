import sys
sys.stdin = open(r'C:\Users\SSAFY\vscode_psb\class_algo\250829\5174.txt', 'r')

T = int(input())

E, N = map(int, input().split())
arr = list(map(int, input().split()))

V = E + 1
left, right = [0] * (V + 1), [0] * (V + 1)

for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
print(arr, left, right)

def pre_order(T):
    if T == 0:
        return 0
    l = pre_order(left[T])
    r = pre_order(right[T])
    return l + r + 1