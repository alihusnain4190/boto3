# turnary operator
# this is simple function which we use to return if age is over 18 True


def is_default(age):
    if age > 18:
        return 'ali'
    else:
        return 'husnain'


print(is_default(19))

# Using turnary we can make it simple


def is_default1(age):
    return True if age > 18 else False


print(is_default1(19))


# Multi line string

print(""" 
ali
    hello

byee
""")

# String methon
# upper , lower , tilte (which meake each string capital), isLower. isUpper,endsWith, startWith
# replace , # find , split ,join (append for sting) ,strip (white space between string), len


# NOTe for these method  they all return new string

name = "hsunain"
print("hu" in name)  # this will give you True if hu will be togather in your string


name = "husnain"
print(name[1:3])

name = "my name is ali"
print(name[2:5])
