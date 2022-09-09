# Dict
dog = {"dog1": 'name-dog', "age": 12, "color": "green"}

print(dog)
# Get name of dog1 we can use two way
print(dog["dog1"])  # 1
print(dog.get("dog1"))

# if color is not exist then it will return pink, If exist it will return green
print(dog.get("colors", "pink"))

# POP method to delete value from list
print(dog.pop("age"))

# output is this without Dog age {'dog1': 'name-dog', 'color': 'green'}
print(dog)

# popItem()  it will delete last item in dict

# we can also check key is exist in dict or not

print("dog1" in dog)


# we can also get all ket from dict

print(dog.keys())
print(list(dog.keys()))

# we can also get values from dic

print(dog.values())
print(list(dog.values()))


# Item
print(dog.items())  # It will return all item and convert into list
print(list(dog.items()))


# insert value into list

dog["fav-food"] = "Meat"
print(dog)

# delete single item from dict
del dog["color"]
print(dog)

# copy dic to other
dogCopy = dog.copy()
print(dogCopy)
