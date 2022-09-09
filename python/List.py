dogs = [1, "ali", True, "hus"]
print(dogs[1])

print(1 in dogs)  # to check 1 is in list or not return True

dogs[2] = 12  # It will replace True with 12

print(dogs)


print(dogs[1:3])  # it will slice from ali to 12

print(dogs[:3])  # it will slice last one

print(len(dogs))  # return total len of list

dogs.append('False')  # It will append False end of list
print(dogs)

dogs.extend(['123', '213'])
print(dogs)  # By using extend you can add multiple value in one time


dogs.remove("ali")
print(dogs)  # it will remove ali from list


print(dogs.pop())  # it remove end of list
print(dogs)


# insert into list
# using inset you can add data at spacific position in list
dogs.insert(0, "husnain")
print(dogs)


# Sort method to sort all list
# need to remeber sort Method move Upper case letter first and lower case at end

num = [1, 3, 5, 2, 5, 2, 6, 3]
num.sort()
print(num)

newnum = num[:]   # Copy of list
print(newnum)
print(num)


# if you want to create new list without modified old list
data = ["ali", "husnain", "ch", "Ali"]
print(sorted(data))

print(data)
