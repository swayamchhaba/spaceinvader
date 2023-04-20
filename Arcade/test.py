def fib(n):
    l = [0, 1]

    while l[-1] < n:
        l.append(l[-2] + l[-1])

    l.pop()
    return l


for i in range(len(fib(100)) - 1):
    print(fib(100)[i], end=", ")

print(fib(100)[-1])
