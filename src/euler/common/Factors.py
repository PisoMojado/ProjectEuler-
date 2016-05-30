def produce_prime_factors(num):
    factors = []
    prime_factor = 2
    while num > 1:
        power_count = 0
        while num % prime_factor == 0:
            power_count += 1
            num /= prime_factor
        if power_count > 0:
            factors.append({prime_factor, power_count})
    return factors


def get_largest_prime_factor(num):
    # works by dividing out all factors until we arrive at the last one, which is the largest
    i = 2
    while i * i <= num:
        while not num % i:
            num /= i
        else:
            if num != 1:
                i += 1
            else:
                num = i
    return num


def produce_all_factors(num):
    prime_factors = produce_prime_factors(num)
    expanded_primes = map(lambda x: [x[0] ** i for i in range(x[1] + 1)], prime_factors)
    raise ValueError("THIS IS INCOMPLETE")


def calculate_factor_count(num):
    return reduce(lambda x, y: x*y, map(lambda x: x[1] + 1, produce_prime_factors(num)), 1)
