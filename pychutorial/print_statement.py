# The print() function is a built-in function. It prints/outputs a specified message to the screen/console window.
# To call a function (this process is known as function invocation or function call) 
# Python strings are delimited with quotes, e.g., "I am a string" (double quotes), or 'I am a string, too' (single quotes).
# Ref: netacad

# ------------------ COMMENT ------------------ #

# this is one line comment
'''
This is a multiline comment
This is a multiline comment
This is a multiline comment
This is a multiline comment
This is a multiline comment

'''

# ------------------ PRINT STATEMENT ------------------ #

print("Hello world! 1") # Generic print method
greetings = "Hello world! 2" # Print using variable
print(greetings)

# ------------------ PRINT WITH CONCATENATION & SEPERATOR ------------------ #

line1 = "hell"
line2 = "o"
# with concatenation/positional argumant
print(line1+line2) # 2 combined string without a space
# with seperation/multiple arguments
print(line1,line2) # 2 combined string with a space
# Sep = Seperator 
print("pu", "ta", "ngi", "na", "mo.", sep="-") 
# Output: pu-ta-ngi-na-mo.

# ------------------ PRINT WITH VARIABLES ------------------ #

first_name = "Tite"
last_name = "Kubo"

print("Hello, my name is "+ first_name, last_name, ". I am the author of bleach")

# print blank line (Escape/Newline)
print("Tiiiiiiiiiii")
print() # Just next line
print("Teeeeeeeeeee")

# ------------------ NEXTLINE INSIDE THE PRINT FUNCTION ------------------ #

print("mahal \nketa \n sobra")
# Output:
# mahal
# keta
#  sobra

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****") # try to print

# ------------------ PRINT using 'end' PARAMETER ------------------ #

print("ti", end=" ")
print("te")
# Output: ti te

# ------------------ MIXED IN ONE INVOCATION ------------------ #

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

# ------------------ HOW TO USE '\' (backslash) THIS IN PRINT FUNCTION ------------------ #
print("idol\\idok")
# Output: idol\idok

print('I\'m Monty Python.') # Output: I'm Monty Python.
print("I'm Monty Python.") # Output: I'm Monty Python.


# ------------------ LAB   Python literals - strings ------------------ #
# ------------------ LAB   Python literals - strings ------------------ #
# ------------------ LAB   Python literals - strings ------------------ #
# Scenario
# Modify the first line of code in the editor, using the sep and end keywords, to match the expected output. Use the two print() functions in the editor.
# 
# Don't change anything in the second print() invocation.
# 
# Expected output
# Programming***Essentials***in...Python

# Answer:
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

# ------------------ MULTIPLE LINE PRINT ------------------ #

print("      *      "*2)
print("     * *     "*2)
print("    *   *    "*2)
print("   *     *   "*2)
print("  ***   ***  "*2)
print("    *   *    "*2)
print("    *   *    "*2)
print("    *****    "*2)


# Scenario
# Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.
# Expected output:
# "I'm"
# ""learning""
# """Python"""

print("I'm\n" + "\"learning\"\n" + "\"\"Python\"\"\n")




# ------------------ TITLE, LOWERCASE AND UPPERCASE ------------------ #

print("hello, world".title()) # Output: Hello, World
print("hAha".upper()) # Output: HAHA
print("hAha".lower()) # Output: hehe

# ------------------ CHANGE/REPHRASE WORD ------------------ #

print("Hello, world".replace("world", "Mark")) # Output: hello, Mark

# ------------------ CENTER A LINE ------------------ #

print("hello po".center(20, "-").upper())
# Output:   
# ------HELLO PO------


# ------------------ JUSTIFY (LEFT AND RIGHT) ------------------ #

# Order menus
print("Americano".ljust(20, "."), "Pesos 90".rjust(4))
print("Cofee".ljust(20, "."), "Pesos 50".rjust(4))
print("Cofficino".ljust(20, "."), "Pesos 120".rjust(4))
print("Mocha".ljust(20, "."), "Pesos 50".rjust(4))
# Output:   
# Americano........... Pesos 90
# Cofee............... Pesos 50
# Cofficino........... Pesos 120
# Mocha............... Pesos 50


# ------------------ LENGTH FUNCTION ------------------ #

# Determine the number of characters in the line
print(len("sadddddddddddddddddddddddddddddddddddddddddddddddddddddddd")) # Output: 58


# ------------------ STRING INDEX VALUES ------------------ #

print("mark"[-1]) # Output: k
print("mark"[0]) # Output: m
print("mark"[1]) # Output: a
print("mark"[2]) # Output: r
print("mark"[3]) # Output: k

print("mark"[1:3]) # 1, Output: ar
print("mark"[1:])  # 2, Output: ark
#   m   a   r   k
#   0   1   2   3   
#       ↑   ↑       ------ 1
#       ↑   ↑   ↑   ------ 2





