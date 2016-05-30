from euler.common.PythagoreanTriples import generate_triple_products

triple_products = {}
generate_triple_products(triple_products, 2, 1, 1)
generate_triple_products(triple_products, 3, 2, 1)

trials = int(raw_input())
for i in range(trials):
    current_N = int(raw_input())
    if current_N in triple_products:
        print(triple_products[current_N])
    else:
        print(-1)
