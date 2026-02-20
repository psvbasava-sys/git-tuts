# Python Integer

# Create a first Python Integer
whole_num = 5  # Whole_num equals five. The Python Integer is created through assignment
print(whole_num)  # 5

# Create more integers and add them together to create new integers through assignment
num_two = 3 # Integer value
num_three = num_two + whole_num  # An Integer value plus an Integer value is an Integer value
print(num_three) # 8

# Test subtraction, multiplication, and division
# Subtraction
num_four = whole_num - num_two  # An integer value minus an integer value is an integer value.
print(num_four) # 2

# Multiplication
num_five = num_four * num_three # An Integer value multiplied with an Integer value is an Integer value
print(num_five) # 16

# Division
num_six = num_five / whole_num # two Integer values divided with each other returns a float if a single divisor sign is used
print(num_six) # 16/5 or 3.2

# Type checking
print(type(num_five)) 
print(type(num_six))

# Floor Division
num_seven = num_five // whole_num # two Integer values floor divided with each other creates a rounded Integer.
print(num_seven)  # 16//5 = 3
print(type(num_seven))

# Integers can be used to keep track of loops
for x in range(1, 6):
    print(x)

# Other datatypes can “if suitable” be converted to or cast as Integers
num_eight = int(5.5)  # Casts the float 5.5 to an integer 5
num_nine = int("3") # Casts the string 3 to an integer 3
print(num_eight)
print(type(num_eight))
print(num_nine)
print(type(num_nine))
