# List

a = [57, 67, 77, 87, 97, ]                   # Create a list of 5 elements

a.append(107)                                # Add at end
print(a)

a.insert(0,47)                               # Add at an particular location
print(a)

a.remove(77)                                 # Remove an value
print(a)

print(max(a))                                # Maximum number
print(min(a))                                # Minimum number

a.reverse()                                  # Reverse a list
print(a)

print(a.count(57))                           # Count a value

b = [66, 44, 44, 33, 22]                     # Remove duplicates from list

result = []

for item in b:
    if item not in result:
        result.append(item)

print(result)

list = [10, 30, 50, 90]                      # Rotate list by k positions

lst = [10, 30, 50, 90]
k = 1

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]

print(rotated)

c = [100, 200, 300, 400, 500]                # Find the second largest number

largest = max(c)
c.remove(largest)

second_largest = max(c)

print(second_largest)

a = [[1, 2], [3, 4], [5, 6]]                 # Flatten a nested list

flat = []

for sublist in a:
    for item in sublist:
        flat.append(item)

print(flat)


# Tuple

t = (9, 13, 7, 57, 40)                       # Create a tuple with 5 elements

print(t)

print(t[0])                                  # Acess first and last elements
print(t[4])

print(t.count(57))                           # Count occurence of an element

print(max(t))                                # Maximum number
print(min(t))                                # Minimum number

a = (50, 90, 50)                             # Convert tuple  → list  → modify  → back to tuple

temp_list = [X for X in a]

temp_list.append(80)
a = tuple(temp_list)

print(a)

t = (10, 20, 30, 40, 50, 60)                 # Slice a tuple to get middle elements

mid = t[1:-1]
print(mid)

b = (10, 15, 20, 25)                         # Check if an element exists

print(20 in b)

c = (8, 9, 10)                               # Swap two tuples
d = (5, 4, 3)

c, d = d, c

print(c)
print(d)

t = (1, 2, 3, 4, 5, 6)                       # Find all pairs in tuple whose sum = target
target = 7

pairs = []

for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i] + t[j] == target:
            pairs.append((t[i], t[j]))

print(pairs)                                 # Remove duplicates from tuple manually

a = (55, 56, 55, 90, 90)

b = set(a)

print(tuple(b))


# Set

s = {30, 50, 60, 40}                          # Create a set and print element

print(s)

s.add(70)                                     # Add and remove elements

s.remove(30)

print(s)

print(40 in a)                                # Check membership of an element

set1 = {4, 8, 9}                              # Perform union of two sets

set2 = {6, 5, 3}

print(set1.union(set2))

print(set1.intersection(set2))                # Intersection of two sets

print(set1.difference(set2))                  # Difference between two sets

list = [44, 54, 65, 65]                       # Converts list with duplicates into a set

print(set(list))

a = {7, 13, 20,}                              # Find symmetric difference

b = {8, 14, 21}

print((a - b) | (b - a))

x = {10, 11, 12}                              # Check if two sets are disjoint

y = {13, 14, 15}

print(x.isdisjoint(y))

s1 = {4, 7, 8, 9}                             # Find common elements in multiple sets

s2 = {7, 9 ,6, 10}

s3 = {6, 9}

print(s1.intersection(s2, s3))


# Dictionary

student = {                                      # Create a dictionary print keys & values
    "name": "Arjun",
    "age": 21,
    "marks": 85
}

print(student.keys())
print(student.values())

student["marks"] = 85                             # Add and update a key-value

print(student)

del student["age"]                                # Delete a key from dictionary

print(student)

a = [1, 2, 2, 3, 1, 4, 2]                         # Count frequency of element in a list using dictionary

freq = {}

for item in a:
    freq[item] = freq.get(item, 0) + 1

print(freq)

d1 = {"a": 1, "b": 2}                              # Merge two dictionaries

d2 = {"c": 3, "d": 4}

d1.update(d2)

print(d1)

d = {"a": 3, "b": 1, "c": 2}                       # Sort dictionary by values

sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))

print(sorted_dict)

d = {"a": 10, "b": 25, "c": 15}                     # Get key with maximum value

max_key = max(d, key=d.get)

print(max_key)

words = ["hi", "hello", "bye", "code", "python"]    # Group words by their length

group = {}

for word in words:
    group.setdefault(len(word), []).append(word)

print(group)

s = "aabbcdeff"                                      # Find first not-repeating character in a string

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

students = {1: "Harika", 2: "Haru", 3: "Har"}        # Student management system using dictionary

print(students)


