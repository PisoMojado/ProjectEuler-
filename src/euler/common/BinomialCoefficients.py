from euler.common.Factorial import factorial
from euler.common.Factorial import factorial_mod_m


def naive_binomial(n, k):
    if n < k:
        raise ValueError("k must be <= n")
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial(n, k):
    if n < k:
        raise ValueError("k must be <= n")
    if (n - k) < k:
        return factorial(n, k + 1) / factorial(n - k)
    else:
        return factorial(n, (n - k) + 1) / factorial(k)

# NOTE: this function does not appear to correct, because
# (factorial(n) / factorial(k)) % m != factorial_mod(n, m) / factorial_mod(k, m)
# def binomial_mod_m(n, k, m):
#     if n < k:
#         raise ValueError("k must be <= n")
#     if (n - k) < k:
#         return factorial_mod_m(n, m, k + 1) / factorial_mod_m(n - k, m)
#     else:
#         return factorial_mod_m(n, m, (n - k) + 1) / factorial_mod_m(k, m)
