def divisible_by_b(a, b):
    x = a + 1
    if x % b == 0:
        return x
    else:
        return divisible_by_b(a + 1, b)

print(divisible_by_b(14, 11))