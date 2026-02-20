# Python Dictionary


# Create a python dictionary with 3 key-value pairs consisting of a key string and a value string
Mailcat = {"Joe":"joe.joe@gmail.com","Anand":"anand.anand@aol.com","Lisa":"lisa@gmx.com"}
print(Mailcat)
print(type(Mailcat))

# Add a new instance "Mohammed" to the dictionary
Mailcat["Mohammed"]="mohammed@gmail.com"
print(Mailcat)

# A dictionary is created with a name, the equality sign and two curly brackets name = {}

# Add an integer key, string instance to the Mailcat to show its versatility.

Mailcat[5] = "This is a string with an integer key"

# Show some ways to address and print the Dictionary keys and items
print(Mailcat.keys())
print(Mailcat.values())
print(Mailcat.items()) # prints the Mailcat dictionaries key-value pairs as a tuple with a list. Manual note: referred to as a "not-a-set-set-like" construct in Python 
# docs. Experts are not united whether its a list inside a tuple or a special view-object or a set and a list combined. 

print(Mailcat["Lisa"])  # prints the value of the "Lisa" key-value pair
print(Mailcat[5]) # prints the value for the 5 integer key
print(Mailcat.get("Lisa")) # Returns the value for key in the dictionary; if not found returns a default value.

# Note that key names must be correctly specified with UPPER case characters or lower-case characters wherever appropriate.

# To change the data value of a key in a dictionary, type:
Mailcat["Joe"] = "joe2.joe2@gmail.com"
print(Mailcat) # As you can see a key's value can be changed with assignment

# To delete a key-value pair you type
del Mailcat[5]
print(Mailcat)

# Some Advanced Dictionary functions. If these feel complex right now – return to this video after completing the entire Python section. 
# If these functions still feel complex, try the Pandas section or course, and return again – all will be clear with practice and exercise makes the master.

# Start with the len() function which gives us the number of elements or key-value pairs in a Dictionary
print(len(Mailcat))

# The Str() function creates a string of a whole dictionary. This may be useful in some Text Mining applications
print(str(Mailcat))  # returns and prints the Mailcat dictionary as a string within curly brackets.

# This for-loop iterates through all the keys in a dictionary and prints each key on a new line.
for m in Mailcat:
    print(m)

# Explicitly
for k in Mailcat.keys():
  print(k)

# Explicitly values
for v in Mailcat.values():
    print(v)

# This loop iterates through all key-value pairs in our dictionary and prints each key-value on a new line.
for k, v in Mailcat.items():
    print(k, v)


# Nested Dictionaries…
Mailcat["spec_mail"]= {"Rolf":"rolf.ag@gmail.com","Anne":"irine.anne@hotmail.com"}
print(str(Mailcat))  # This a nested Dictionary with a complex multi-type structure 

# Currently no inbuilt easy-accessible Python function to handle multi-type strucutures

# For-loop using the direct known adress of a part of the multi-type structure
for k, v in Mailcat["spec_mail"].items():
    name, adress = k, v
    print(name, adress)

# Using the keys and direct known adress of a exactly defined part of the multi-type structure (many possible solutions)
print(list(Mailcat["spec_mail"].keys())[0])
print(Mailcat["spec_mail"]["Rolf"])

# "Not-so-pythonic" automation variant (makes it possible to list and adress key-value pairs using list position notation)
print(list(Mailcat["spec_mail"].keys())[0])
print(Mailcat["spec_mail"][list(Mailcat["spec_mail"].keys())[0]])

print(list(Mailcat["spec_mail"].keys())[1])
print(Mailcat["spec_mail"][list(Mailcat["spec_mail"].keys())[1]])

# Use "pythonic" automation to "flatten" the Mailcat dictionary to a standard dictionary and delete the nested dictionary
for k, v in Mailcat["spec_mail"].items():
    Mailcat[k] = v
del Mailcat["spec_mail"]
print(Mailcat)


# How to clear or delete a Dictionary
Mailcat.clear() # deletes all elements in a dictionary.
print(Mailcat)
del Mailcat  # deletes the Dictionary
# print(Mailcat) # Error
# if you type print(Mailcat) here, the error shows that the Mailcat object no longer exists.













