import sys
import os
os.chdir(r'C:\vscode_psb\class_algo\250910')
sys.stdin = open('11892.txt', 'r')


def quicksort(arr, low, high):

    if low < high:
        pivot_index = partition(arr, low, high)
        
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    quicksort(arr, 0, N - 1)
    
    middle_element = arr[N // 2]
    print(f"#{tc} {middle_element}")