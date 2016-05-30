def get_substring_product(string, length):
    product = 1
    for j in range(length):
        product *= int(string[j])
    return product


def get_substring_products(N_string, N_length, k):
    products = []
    for j in range(N_length - k):
        products.append(get_substring_product(N_string[j:j+k], k))

    return products


trials = int(raw_input())
for i in range(trials):
    line = map(int, raw_input().split())
    N_string = str(raw_input())
    largest_product = reduce(lambda x, y: y if x < y else x,
                             get_substring_products(N_string, line[0], line[1]))
    print(largest_product)
