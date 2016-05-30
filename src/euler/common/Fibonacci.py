class FibonacciSeries(object):
    def __init__(self, ceiling):
        self.num_1 = 1
        self.num_2 = 1
        self.ceiling = ceiling

    def __iter__(self):
        while self.num_2 < self.ceiling:
            value = self.num_2
            self.num_2 += self.num_1
            self.num_1 = value
            yield value
        raise StopIteration


def produce_series_under_n(n):
    fib_iter = FibonacciSeries(n)
    return [x for x in fib_iter]
