# from itertools import product, izip_longest
# 
# template_hash_loop = """
#     for item in {var_collection}:
#         hash_to_data[{code_hash_item}][{collection_number}].append(item)
# """
# template_inner_join_yield_tuples = """
#     for groups in hash_to_data.values():
#         yield from product(*groups)
# """
# template_left_join_yield_tuples = """
#     for groups in hash_to_data.values():
#         left_length = len(group[0])
#         yield from product(
#             group[0],
#             *(
#                 group if group else [None]
#                 for group in groups[1:]
#             )
#         )
# """
# template_outer_join_yield_tuples = """
#     for groups in hash_to_data.values():
#         max_length = max(len(group) for group in groups)
#         yield from product(
#             *(
#                 group if len(group) == max_length else group + [None] * (max_length - len(group))
#                 for group in groups
#             )
#         )
# """
# 
# from convtools import conversion as c
# 
# 
# 
# 
# 
# 
# c.input_arg("right").pipe(
#     c.aggregate(
#         c.reduce(
#             c.ReduceFuncs.DictArray,
#             (c.item(0), c.this()),
#             default={}
#         )
#     ),
#     label_output="hash_to_items",
# ).pipe(
#     c.input_arg("left").pipe(
#         c.inline_expr('''((left_item, right_item) for left_item in {left_items} for right_item in {right_items})''').pass_args(
#             left_items=c.this(),
#             right_items=c.inline_expr("left_item").item(0).pipe(
#                 c.if_(
#                     c.this().in_(c.label("hash_to_items")),
#                     c.label("hash_to_items").item(c.this()),
#                     c.naive(()),
#                 )
#             )
#         ),
#     )
# ).gen_converter(debug=True, signature="left, right")
# 
# 
# 
# def inner_join(hash_to_left_item_gen, hash_to_right_items):
#     for left_item_hash, left_item in hash_to_left_item_gen:
#         if left_item_hash in hash_to_right_items:
#             for right_item in hash_to_right_items[left_item_hash]:
#                 yield left_item, right_item
# 
# j = c.input_arg("right").pipe(
#     c.aggregate(
#         c.reduce(
#             c.ReduceFuncs.DictArray,
#             (c.item(0), c.this()),
#             default={}
#         )
#     ),
#     label_output="hash_to_right_items",
# ).pipe(
#     c.input_arg("left").pipe(
#         c.generator_comp(
#             (c.item(0), c.this())
#         )
#     )
# ).pipe(
#     c.call_func(inner_join, c.this(), c.label("hash_to_right_items"))
# ).gen_converter(debug=True, signature="left, right")
# 
# abc = 1
# def f():
#     return len([abc for i in range(1000000)])
# %timeit f()
# 
# 
# abc = 1
# def f():
#     return len([globals()['abc'] for i in range(1000000)])
# %timeit f()
# # 103 ms ± 611 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
# 
# abc = 1
# def f():
#     return len([abc for i in range(1000000)])
# %timeit f()
# # 54.7 ms ± 452 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
# 
