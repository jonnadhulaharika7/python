# Weather temperature analysis system using built-in-functions

# Weekly temperature in celsius
temperatures = [30, 32, 28, 31, 29, 27, 33]

# print() function
# Display all temperatures
print("Weekly temperatures:", temperatures)

# len() function
# Counts total number of days
print("total days recorded:", len(temperatures))

# max() function
# Finds maximum temperature
print("Highest temperature:", max(temperatures))

# min() function
# Finds minimum temperature
print("Loewst temperature:", min(temperatures))

# sum() function
# Calculates total temperatures 
print("Total temperature:", sum(temperatures))

# type() function
# Check data type of temperatures
print("Data type of temperatures:", type(temperatures))

# Sorted() function
# Sort temperatures in ascending order
print("Sorted temperatures:", sorted(temperatures))

# abs() function
# Finds temperature differnce from normal temperature (25 degrees)
differnce = abs(25 - max(temperatures))
print("Differnce from normal Temperature:", differnce)

# round() function
# Rounds average temperature
print("Average temperature:", round(sum(temperatures) / len(temperatures), 2))

# input() function
# Takes city name from user
city = input("Enter city name:")

# print() function
# Display final message
print("Weather report generated for", city)




# Find length without using len() 
numbers = [99, 89, 69, 59]
count = 0
for num in numbers:
    count = count + 1
print("Length of list is:", count)

# Find maximum wthout using max()
numbers = [99, 89,69, 59]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum value is:", maximum)

# Find minimum without using min()
numbers = [99, 89, 69, 59]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print("Minimum value is:", minimum)
