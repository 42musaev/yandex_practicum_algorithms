def get_value_function(a, x, b, c):
    return (a * (x ** 2)) + (b * x) + c


a, x, b, c = map(int, input().split())
print(get_value_function(a, x, b, c))
