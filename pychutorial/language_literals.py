# Literals are notations for representing some fixed values in code. Python has various types of literals - for example, a literal can be a number (numeric literals, e.g., 123), or a string (string literals, e.g., "I am a literal.").
# Literals = Data type (It can hold any value type, such as strings, numbers, and more)

# ------------------ INTEGERS ------------------ #

print(123) # The interpreter will see this as integers (A series of numbers)
print("123") # The interpreter will see this as string (A series of letters)
# Same output but different literals

# You can use underline/underscore(_) to seperate to become more readable to developer
print(1) # Ones
print(10) # Tens
print(100) # Hundreds
print(1000) # Thousands
print(10_000) # Ten Thousands
print(100_000) # Hundred thousands
print(1_000_000) # Millions

# ------------------------------------ #

print(1_000_000) # Output: 1000000
print(1,000,000) # Output: (1,000,000)
# note: when you use commas in the integers, the interpreter will see this as a multiple arguments
# Do not use comma to seperate numbers but the underline instead

# ------------------------------------ #

# In integers, you can also use negative numbers just by adding negative symbol(-)
print(1_000_000) # Positve
print(-1_000_000) # Negative

# ------------------ OCTAL AND HEXADECIMAL NUMBERS ------------------ #

# If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value
# 0o123 is an octal number with a (decimal) value equal to 291
print(0o123)

# ------------------ FLOATS ------------------ #

# Floats are just basically a decimal number
print(3.14) # Output: 3.14
print(-3.14) # Output: -3.14
print(.14) # Output: 0.14
print(0.14) # Output: 0.14

# ------------------ INTS VS FLOAT ------------------ #

print(1) # The interpreter will see this as integers
print(1.0) # The interpreter will see this as float

# ------------------------------------ #

print(3e1) # Output: 30.0
print(3e2) # Output: 300.0
print(3e3) # Output: 3000.0
print(3e4) # Output: 30000.0
print(3e5) # Output: 300000.0
# 3 = Base number
# e/E = Exponent
# after exponent = times ten to the power of

# ------------------ CODING FLOATS ------------------ #

print(0.000000000000000000000000000000000662607) 
# # Output: 6.62607E-34 (6.62607 x 10-34)

print(0.0000000000000000000001)
# # Output: 1e-22

# ------------------ BOOLEAN VALUES ------------------ #

print(True) # Output: True
print(False) # Output: False

print(True > False) # True is greater than False
print(True < False) # True is less than False
# Note: Just think about the bigger value 

# ------------------ EXTRA ------------------ #
' There is one more, special literal that is used in Python: the None literal. '
' This literal is a NoneType object, and it is used to represent the absence of a value.  '
' We will tell you more about it soon. '



