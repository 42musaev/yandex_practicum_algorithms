def check_chaotic_temperature(temperature_of_days):
    chaotic_days = 0
    n = len(temperature_of_days)

    if n == 1:
        return 1

    for idx in range(1, n - 1):
        current_temp = temperature_of_days[idx]
        pre_temp = temperature_of_days[idx - 1]
        after_temp = temperature_of_days[idx + 1]

        if current_temp > pre_temp and current_temp > after_temp:
            chaotic_days += 1

    if temperature_of_days[0] > temperature_of_days[1]:
        chaotic_days += 1
    if temperature_of_days[n - 1] > temperature_of_days[n - 2]:
        chaotic_days += 1

    return chaotic_days


_ = input()
temperature_of_days = list(map(int, input().split()))
print(check_chaotic_temperature(temperature_of_days))
