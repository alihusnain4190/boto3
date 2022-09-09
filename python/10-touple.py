# we use Touple for immutable list
num = (1, 2, 3, 4, 5)


print(num)

# Get first item from touple
print(num[0])


# check value exist or not
print(2 in num)


# if you want to add new value in touple but do not modified orignal touple

newValue = num+(10, 12)
print(newValue)
print(num)
