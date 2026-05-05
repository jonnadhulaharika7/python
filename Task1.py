# Strings are used to store text

# STRINGS

name = "harika"
print(name.upper())
print(name.lower())
print(name.title())
print(name.find("i"))
print(name.startswith("ha"))
print(name.endswith("ka"))
print(name.replace("harika","haru"))
print(name.split())
print(name.count("h"))
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.islower())
print(name.isupper())
print(name.isspace())


# List is an built in data structure used to store multiple items in a single variable
# 1.ordered index
# 2.mutable
# 3.allows duplicates
# 4.allows indexing
# 5.hetrogenous - numz , char

numbers = [99, 89, 69, 69, 59]

print(numbers)
print(numbers[0])
print(numbers[-1])

# List METHODS

a = [99,89,79]

a.append(69)          # Add at end
print(a)

a.insert(4,59)        # Insert at position
print(a)

a.remove(99)          # Remove item
print(a)

a.pop()               # Remove last item
print(a)

a.sort()              # Sort list
print(a)

a.reverse()           # Reverse list
print(a)

a.extend([49,39])     # Add multiple values
print(a)

print(len(a))        # Length of list
print(max(a))        # Maximum value
print(min(a))        # Minimum value


# Numeric operations

a = 13
b = 7

print(a + b)           # Addition
print(a - b)           # Subraction
print(a * b)           # Multiplication
print(a / b)           # Division
print(a // b)          # Floor division
print(a % b)           # Modulus
print(a **b)           # Power