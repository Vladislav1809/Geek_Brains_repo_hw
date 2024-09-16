# Number_1
"""
def odd_nums(finish_number):
    x = 1
    while x <= finish_number:
        yield x
        x += 2


odd_to_15 = odd_nums(15)
"""
# Number_2
finish_number = 15
odd_nums_generator = (x for x in range(1, finish_number + 1, 2))
print(next(odd_nums_generator))
# print(next(odd_nums_generator))
