def check_same_parity(a, b, c):
    if a % 2 == b % 2 == c % 2:
        print('WIN')
    else:
        print('FAIL')


a, b, c = map(int, input().split())
check_same_parity(a, b, c)
