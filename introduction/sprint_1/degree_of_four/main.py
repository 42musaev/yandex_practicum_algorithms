n = int(input())
if n <= 0:
    print(False)
while n % 4 == 0:
    n //= 4
print(n == 1)
