lst = [0, 1, 7, 2, 4, 8]
if not lst:
    result = 0
else:
    doubles_numbers = sum(lst[i]for i in range(0, len(lst), 2))
    max_element = lst[-1]
    result = doubles_numbers * max_element
print(result)
lst = []
if not lst:
    result = 0
else:
    doubles_numbers = sum(lst[i]for i in range(0, len(lst), 2))
    max_element = lst[-1]
    result = doubles_numbers * max_element
print(result)

