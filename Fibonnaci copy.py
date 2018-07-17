n = 50


# determines the value of the nth index in the fibonacci sequence

def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(n))
