# input data
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# number 4
result = [x for i, x in enumerate(src) if src[i] > src[i-1] and i != 0]
print(result)
