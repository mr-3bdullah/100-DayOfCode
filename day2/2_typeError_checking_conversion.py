# wellcom in 2sec lesson.

# ----> as we know len | not work with numbers.

# ------------- Ex: ----------------

# char_num = len(input("type your name: "))
# print("you have " + char_num + " characters.")

# when try it will give you :
# ! TypeError: can only concatenate str (not "int") to str.

# becouse char_num his type is -> int (integer).
# * we cant concatenate => string with int.

# ----------> solve <-------------

# to solve this type of error , shoud know kind of my data.
#  we use type() | function to know it.

# ====> EX:
print(type(1))  # <class 'int'>
print(type(12.3))  # <class 'float'>
print(type("abdullah"))  # <class 'str'>

# ----> use case:

# char_num = len(input("type your name: "))
# print(type(char_num)) # <class 'int'>

# ~> we have two way to fix :
# 1: conver the type of char_num
# 2: make our input store strin.
# --------

# ##=> 1:

# =======> this soultion call -> converting
#
# convertin meain => change type of (data type) to anouther

char_num = len(input("type your name: "))

char_num = str(char_num)
print(type(char_num))  # <class 'str'>
print("you have " + char_num + " characters.")

# -----------

# ##=> 2:

char_num = str(len(input("type your name: ")))
print("you have " + char_num + " characters.")
