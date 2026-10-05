number = input("Enter a number: ")
result = number.replace("-","")
sum = 0
for num in result:
    if num.isdigit():
        sum += int(num)
print(sum)
