lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = [x for x in lst if x != 0]
result.extend([0] * (len(lst) - len(result)))
print(result)