import operator


def factorial(n, halt_num=1):
    if halt_num > n:
        raise ValueError("halt_num must be <= n")
    if n < 0:
        raise ValueError("Can't solve factorials for negative numbers.")
    if n == 0:
        return 1
    else:
        return reduce(operator.mul, range(halt_num, n+1))


def factorial_mod_m(n, m, halt_num=1):
    if halt_num > n:
        raise ValueError("halt_num must be <= n")
    if n < 0:
        raise ValueError("Can't solve factorials for negative numbers.")
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * (y % m), range(halt_num, n+1)) % m
