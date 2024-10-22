# ------------------ OPERATORS AND THEIR PRIORITIES ------------------ #





# ------------------ EXAMPLE OF VARIABLES ------------------ #

# List of example that can be use as a variable
# MyVariable
# i
# l
# t34
# Exchange_Rate
# counter
# days_to_christmas
# TheNameIsTooLongAndHardlyReadable
# _
# Adiós_Señora
# sûr_la_mer
# Einbahnstraße
# переменная

# List of example that cannot be use as a variable
# 10t (does not begin with a letter)
# !important (does not begin with a letter)
# exchange rate (contains a space).

# ------------------ EXAMPLE OF PREDEFINED/RESERVED KEYWORDS ------------------ #

# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 
#  'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
#  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Note: You cannot name a variable using of these

# When you see other color in a variable, it means it cannot be use in the program.

# ------------------ ADDING VALUE INSIDE THE VARIABLE ------------------ #

print("Hello world! 1") # Generic print method 
greetings = "Hello world! 2" # Print using variable
print(greetings) # Output: greetings

var = 1
print(var) # Output: 1

idnum = 1
name = 'John Lemon'
account_balance = 1.20
print(idnum, name, account_balance) # Output: 1 John Lemon 1.20

var = "17"
print("My age: " + var) # Output: My age: 17
print("My age:", var) # Output: My age: 17


var2 = 29
var2 = var2 + 1
print(var2) # Output: 30



# ------------------ LAB   Python Variables ------------------ #
# ------------------ LAB   Python Variables ------------------ #
# ------------------ LAB   Python Variables ------------------ #

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print(total_apples)