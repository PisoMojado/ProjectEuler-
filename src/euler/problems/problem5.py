from euler.common.EratosthenesSieve import produce_primes_under_n


def get_largest_prime_power_under_n(p, n):
    base = p
    while p * base <= n:
        p *= base
    return p


# the solution is the product of all primes which fit under N to the power t,
# where t is their largest exponent that fits under N
trials = int(raw_input())
primes_under_forty = produce_primes_under_n(40)
for i in range(trials):
    current_N = int(raw_input())
    primes_under_n = [x for x in primes_under_forty if x <= current_N]
    if current_N == 1:
        print(1)
    else:
        print(reduce(lambda x, y: x * y, map(lambda x:
                                             get_largest_prime_power_under_n(x, current_N),
                                             primes_under_n)))
