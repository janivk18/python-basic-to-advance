capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}
#print(capitals.get("China"))
if "USA" in capitals:
    print(capitals["USA"])
else:
    print("No capital")
for key in capitals:
    print(capitals[key])
for value in capitals.values():
    print(value)
for key,value in capitals.items():
    print(f"{key}: {value}")
