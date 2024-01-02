_ = input()
arr = list(map(int, input().split()))

arr = [float('inf') if i != 0 else 0 for i in arr]

_count = float('inf')
for i in range(len(arr)):
    if arr[i] == 0:
        _count = 0
    else:
        _count += 1
    arr[i] = min(_count, arr[i])

_count = float('inf')
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == 0:
        _count = 0
    else:
        _count += 1
    arr[i] = min(_count, arr[i])

print(*arr)
