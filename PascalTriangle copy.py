
i = 5
j = 3


def pascalTriangle(a,b):
    if a == b:
        return 1
    if b == 0:
        return 1
    return pascalTriangle(a-1, b-1) + pascalTriangle(a-1, b)

print("The value of the number is:", pascalTriangle(i, j))

