import math

# meaning = 8



# if age < 18:
#     print("You are to young!")
# elif age >= 18:
#     print("Welcome to the club!")

# # Ternary Operator if statements
# print("Right On!") if meaning > 10 else print("Not Today")

# String data type
first = "David"
last = "Hawley"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#Constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation

fullname= first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = "I like country music from the " + decade + "s."
print(statement)

# Multiple lines ''''''
multiline = '''
hey, how are you?

I was just checking in.

                            All good?

'''
print(multiline)

# Escaping special characters
sent = "I'm back at work!\tHey!\n\nWhere's this at\\Located?"
print(sent)

# String methods 
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title);
print(multiline.replace("good", "ok"));

print(len(multiline))
multiline += "                                       "
multiline = "                                              " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a men 
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Cake".ljust(16, ".") + "$5".rjust(4))

print("")


# String index values
print(first[-1])
print(first[1])
print(first[1:])

# SOme methods return boolean data 
print(first.startswith("D"))
print(first.endswith("d"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# Integer Type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, bool))

# Float Type
gpa = 4.0
y = float(1.4)
print(type(gpa))

# Complex type 
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))



print(math.pi)
print(math.sqrt(65))
print(math.ceil(gpa))
print(math.floor(gpa))
