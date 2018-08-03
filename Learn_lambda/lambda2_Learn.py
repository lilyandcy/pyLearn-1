def fn(x):
    return lambda y:x*x + 2*x-4
a=fn(3)
print a(1)