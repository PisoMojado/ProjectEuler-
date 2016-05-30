# for pythagorean triples solution, use pythagorean method to generates all triples
# start with m = 2, n = 1, k = 1 and increment all three variables until you reach 3000
# make sure m and n are co-prime
# as you do so, store all of them using c as the key, and store the product abc
# when you face a key collision, compare the two abc products
# store the larger one
# then run trials and look up values with N as key
# if none is found, return -1; otherwise, return the product
from fractions import gcd


def calculate_triple(m, n, k):
    a = k * (m ** 2 - n ** 2)
    b = k * 2 * m * n
    c = k * (m ** 2 + n ** 2)
    return c, a, b


# for some retarded reasom, the sum of the triple values is the key
def _add_or_update_triple_product(triple_dict, triple):
    product = triple[0] * triple[1] * triple[2]
    sum = triple[0] + triple[1] + triple[2]
    if not sum in triple_dict or product > triple_dict[sum]:
        triple_dict[sum] = product


def generate_triple_products(triple_dict, start_m, start_n, start_k):
    triple = 0, 0, 0
    m = start_m
    n = start_n
    k = start_k
    while calculate_triple(m, n, k)[0] <= 3000:
        while n < m:
            if gcd(m, n) == 1:
                while True:
                    triple = calculate_triple(m, n, k)
                    if triple[0] > 3000:
                        break
                    _add_or_update_triple_product(triple_dict, triple)
                    k += 1
            k = start_k
            n += 2
        k = start_k
        n = start_n
        m += 2