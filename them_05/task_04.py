# Объявите функцию detect_duplicates() с параметром *args

# def detect_duplicates(*args):
#     unic = set()
#     count = 0
#     for num in args:
#         if num in unic:
#             count += 1
#         else:
#             unic.add(num)
#     return count

def detect_duplicates(*args):
    return len(args) - len(set(args))

print(detect_duplicates(1, 2, 3, 4, 5, 1, 2, 3))  # 3
print(detect_duplicates(1, 1, 1))  # 2
print(detect_duplicates(3, 2, 2))  # 1
print(detect_duplicates(4, 2))  # 0
