def sliding_average(sequence, k):
    averages = []
    n = len(sequence)
    if k > n:
        return []

    current_sum = sum(sequence[:k])
    averages.append(current_sum / k)
    for i in range(n - k):
        current_sum -= sequence[i]
        current_sum += sequence[i + k]
        averages.append(current_sum / k)

    return averages


n = int(input())
data = list(map(int, input().split()))
k = int(input())
result = sliding_average(data, k)
print(*result)
