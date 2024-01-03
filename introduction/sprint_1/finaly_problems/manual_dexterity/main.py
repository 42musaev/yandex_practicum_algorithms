k = int(input())
lines = [int(char) for row in [input() for _ in range(4)] for char in row if char.isdigit()]

hash_map = {}
for num in lines:
    if num in hash_map:
        hash_map[num] += 1
    else:
        hash_map[num] = 1

count = 0
for _, v in hash_map.items():
    if v <= k * 2:
        count += 1
print(count)
