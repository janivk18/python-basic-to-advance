numbers = [55,3,22,33,22,11,22,44,2,11,2,77,8,77]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)