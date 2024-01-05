a = input()
b = input()

letter_counter = {}

for i in a:
    if i in letter_counter:
        letter_counter[i] += 1
    else:
        letter_counter[i] = 1

for i in b:
    if i in letter_counter:
        letter_counter[i] -= 1
    else:
        letter_counter[i] = 1

for k, v in letter_counter.items():
    if v != 0:
        print(k)
