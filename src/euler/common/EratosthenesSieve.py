def eratosthenes_sieve_under_n(n):
    """
    Eratosthenes' sieve will produce an array of numbers,
    and another array marking each of those numbers as prime or not (composite)
    """
    all_numbers_under_n = [k for k in range(2, n+1)]
    n_length = len(all_numbers_under_n)
    prime_flags = [True] * n_length
    prime_index = 0
    while prime_index < n_length:
        prime = all_numbers_under_n[prime_index]
        coefficient = 2
        while prime * coefficient <= n:
            # We subtract the first prime, as our array is structured in this way
            prime_flags[prime * coefficient - 2] = False
            coefficient += 1
        prime_index += 1
        while prime_index < n_length and not prime_flags[prime_index]:
            prime_index += 1
    return all_numbers_under_n, prime_flags


def produce_prime_sum_map_under_n(n):
    """
    This function is similar to eratosthene's sieve.
    It creates a map of the sum of all primes under i, for all i <= n
    """
    sieve = eratosthenes_sieve_under_n(n)
    all_numbers_under_n = sieve[0]
    n_length = len(all_numbers_under_n)
    prime_flags = sieve[1]
    prime_sum_hash = {}
    prime_sum = 0
    for k in range(n_length):
        if prime_flags[k]:
            prime_sum += all_numbers_under_n[k]
        prime_sum_hash[all_numbers_under_n[k]] = prime_sum
    return prime_sum_hash


def produce_primes_under_n(n):
    """
    Filters the sieve of numbers into a list of only primes
    """
    sieve = eratosthenes_sieve_under_n(n)
    all_numbers_under_n = sieve[0]
    n_length = len(all_numbers_under_n)
    prime_flags = sieve[1]
    return [all_numbers_under_n[k] for k in range(n_length) if prime_flags[k]]