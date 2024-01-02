_n = input()
arr = list(map(int, input().strip().split()))

distances = [0 if arr[i] == 0 else float('inf') for i in range(len(arr))]

nearest_house = float('inf')
for i in range(len(arr)):
    if arr[i] == 0:
        nearest_zero = arr[i]
    else:
        nearest_house += 1
        distances[i] = min(distances[i], nearest_house)

nearest_house = float('inf')
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == 0:
        nearest_zero = arr[i]
    else:
        nearest_house += 1
        distances[i] = min(distances[i], nearest_house)

print(*distances)
