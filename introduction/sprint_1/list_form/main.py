_ = input()

a = input().replace(' ', '')[::-1]
b = input().replace(' ', '')[::-1]

max_len = max(len(a), len(b))
carry = 0
idx = 0

result = ''
while idx < max_len or carry:
    if len(a) <= idx:
        num_a = 0
    else:
        num_a = int(a[idx])

    if len(b) <= idx:
        num_b = 0
    else:
        num_b = int(b[idx])

    total = num_a + num_b + carry
    result += " " + str(total % 10)
    carry = total // 10
    idx += 1

print(result[::-1])
