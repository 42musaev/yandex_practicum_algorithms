n = int(input())
arr = list(map(int, input().strip().split()))
target_sum = int(input())


def _func(arr, target_sum):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]


r = _func(arr, target_sum)
if r:
    print(*r)
else:
    print(r)
