a = input()
b = input()
l_a = len(a)
l_b = len(b)
max_len = max(l_a, l_b)
idx = 0
result = ''
carry = 0

while idx < max_len:
    if idx < l_a:
        num_a = int(a[l_a - idx - 1])
    else:
        num_a = 0

    if idx < l_b:
        num_b = int(b[l_b - idx - 1])
    else:
        num_b = 0
    total = num_a + num_b + carry
    result = str(total % 2) + result
    carry = total // 2

    idx += 1

if carry:
    result = '1' + result

print(result)
