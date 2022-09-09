# = this euqal sign is for assigment operator
# 1+1 =2  +
# 2-1 =1
# 2*2 =4
# 4 %3 = 1
# 4 ** 2 =16  this is mean power of 2

# we also use + operator for concate

fname = 'ali'
lname = 'husnain'
print(fname + lname)
print("ali" + "husnain")

age = 8
age += 8
print(age)  # age =age +8 => 8+8 =16


# Comparasion operator
# a == b
# a != b
# a > b
# a < b


# Boolean operator
cond1 = False
cond2 = True
not cond1  # Ypu will make oposite turn into True
cond1 and cond1  # mean both has to be true
cond1 or cond1  # mean one of them need to
print(not cond1)  # True


# for Or operator  If first operend is false then return second
print(0 or 1)  # 1
print(False or "hey")  # hey
print('hi' or 'hey')  # hi
print([] or False)  # False
print(False or [])  # []


# And return second if first true, if false it return seoncd
print(0 and 1)  # 1
print(False and "hey")  # hey
print('hi' and 'hey')  # hi
print([] and False)  # False
print(False and [])  # []

# is
# in
