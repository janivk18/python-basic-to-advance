list_of_fruits = ["apple", "banana", "orange", "mango"]
list_of_fruits.append("mango")
list_of_fruits.remove("orange")
list_of_fruits.pop(0)
result = (set(list_of_fruits))
for fruit in result:
    print(fruit,end=" ")
