
# def repair(odd: list, even: list):
#     all_list = odd + even
#     odd = []
#     even = []
#     for num in all_list:
#         if num % 2 != 0:
#             odd.append(num)
#         else:
#             even.append(num)
#     return sorted(odd, reverse=True), sorted(even)

# def repair(odd: list, even: list):
#     all_numbers = odd + even
#     odds = sorted([x for x in all_numbers if x % 2 != 0], reverse=True)
#     evens = sorted([x for x in all_numbers if x % 2 == 0])
#     return odds, evens

# def repair(odd: list, even: list):
#     all_numbers = odd + even
#     odds = sorted(filter(lambda x: x % 2 != 0, all_numbers), reverse=True)
#     evens = sorted(filter(lambda x: x % 2 == 0, all_numbers))
#     return odds, evens

def repair(odd: list, even: list):
    odds, evens = [], []
    for num in odd + even:
        (odds if num % 2 else evens).append(num)
    odds.sort(reverse=True)
    evens.sort()
    return odds, evens


print(repair([1, 2, 2, 1, 2, 1], [3, 4, 4, 3, 3, 4, 4]))
# ([3, 3, 3, 1, 1, 1], [2, 2, 2, 4, 4, 4, 4])
print(repair([2], [1]))  # ([1], [2])
