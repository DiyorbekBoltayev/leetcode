def f(n):
    if n<=3:
        return 5
    return f(n-1)+2*f(n-4)
print(f(9))
