from typing import List


def _func(arr: List[int], k: int):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == k:
            return arr[left], arr[right]

        if current_sum > k:
            right -= 1
        if current_sum < k:
            left += 1


n = int(input())
chips = list(map(int, input().split()))
k = int(input())

pair = _func(chips, k)

if pair:
    print(*pair)
else:
    print("None")
