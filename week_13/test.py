apply = lambda f, x: f(x)
result = apply(lambda n: pow(n, 3), 4)
print(result)


loudify = lambda s: s.upper() + '!!!'
alarm = lambda name: f'Wake up, {name}'
double = lambda x: x * 2