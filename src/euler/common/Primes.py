from euler.common.EratosthenesSieve import produce_primes_under_n


class PrimeSeries(object):
    def __init__(self, ceiling):
        self.prime_series = produce_primes_under_n(ceiling)

    def __iter__(self):
        for prime in self.prime_series:
            yield prime
        raise StopIteration

