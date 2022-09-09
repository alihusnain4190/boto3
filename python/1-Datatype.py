# name = "ali"
# print(name)

# indentation is matter . Every thing belong to block

# Data Type

name = "ali"
# you could check type of string by using type
# print(type(name))

# can see type of name is string or not
print(type(name) == str)  # True


# you could also check is name is instance of string
print(isinstance(name, str))  # REsult True


# For int
age = 30
print(isinstance(age, int))  # Result is True
print(isinstance(age, float))  # Result is False


# you can convert one Data type to other

age = float(30)
print(isinstance(age, float))


# Convert string to int

num = "22"
age = int(num)
print(isinstance(age, int))  # True
# you will get error because you are passing string of charector not string of number
#name = "ali"
#age = int(name)
#print(isinstance(age, int))


# Some other type of data type
# Complex for complex number
# bool for boolean
# list for list
# set for sets
# tuple for tuples
# dict for dictionaries
