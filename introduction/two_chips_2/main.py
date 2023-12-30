def _func(array, k):
    previous = set()

    for num in array:
        current_num = k - num
        if current_num in previous:
            return current_num, num
        else:
            previous.add(num)


n = int(input())
chips = list(map(int, input().split()))
k = int(input())

pair = _func(chips, k)

if pair:
    print(*pair)
else:
    print("None")
