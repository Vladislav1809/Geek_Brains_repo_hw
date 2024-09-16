# input data
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# number 5
final_massive = [x for x in src if src.count(x) == 1]
print(final_massive)