numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
total = 0
for num in numbers:
    for i in num:
        print(i, end=" ")
        total += i
print()
print(f"the total value is {total}")
hight1 = 0
hight2 = 0
hight3 = 0
for number in numbers[0]:
    print(number, end=" ")
    if hight1 < number:
        hight1 = number
for number in numbers[1]:
    print(number, end=" ")
    if hight2 < number:
        hight2 = number
for number in numbers[2]:
    print(number, end=" ")
    if hight3 < number:
        hight3 = number
result = hight1 + hight2 + hight3
print()
print("THe highest value is : ",result)

