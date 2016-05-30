def produce_triangular_numbers(triangle_num_count):
    triangle_nums = []
    natural_num = 1
    current_triangle = 1
    while len(triangle_nums) < triangle_num_count:
        triangle_nums.append(current_triangle)
        natural_num += 1
        current_triangle += natural_num
    return triangle_nums


# triangle_map = collections.OrderedDict({})
# current_natural_num = 1
# current_triangle = 1
# current_triangle_factors = 1
# for i in range(1, 1000):
#     while current_triangle_factors <= i:
#         current_natural_num += 1
#         current_triangle += current_natural_num
#         current_triangle_factors = calculate_factor_count(current_triangle)
#         if get_map_key(current_triangle_factors - 1, triangle_map.keys()) == 0:
#             triangle_map[current_triangle_factors - 1] = current_triangle
# print triangle_map

# This is a growing hash to help with any quick answers we've found
# triangle_map = collections.OrderedDict({})
# trial_count = int(raw_input())
# current_natural_num = 1
# current_triangle = 1
# current_triangle_factors = 1
# for i in range(trial_count):
#     factor_threshold = int(raw_input())
#     map_key = get_map_key(factor_threshold, triangle_map.keys())
#     if map_key > 0:
#         print(triangle_map[map_key])
#     else:
#         while current_triangle_factors <= factor_threshold:
#             current_natural_num += 1
#             current_triangle += current_natural_num
#             current_triangle_factors = calculate_factor_count(current_triangle)
#             if get_map_key(current_triangle_factors - 1, triangle_map.keys()) == 0:
#                 triangle_map[current_triangle_factors - 1] = current_triangle
#         print(current_triangle)
