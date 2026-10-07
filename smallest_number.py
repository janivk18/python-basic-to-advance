numbers = [45,5,3,0,5,2,33,11,222,5]
smallest_num = numbers[0]
for num in numbers:
    if num < smallest_num:
        smallest_num = num
print(f"The smallest number is: {smallest_num}")