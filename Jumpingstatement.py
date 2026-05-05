#Using BREAK statement to exit a loop when a condition is met
books = ["English", "Maths", "science", "History", "Geography"]
for book in books:
    if book == "Geography":
        print("Found the book")
        break
    else:
        print("Searching" , book)



#Using CONTINUE statement to skip an iteration when a condition is met
items = ["Rice", "Wheat", "Sugar", "Salt", "Oil"]
for item in items:
    if item == "Salt":
        print("Salt is out of stock, skipping")
        continue
    else:
        print("Buying", item)



#Using PASS statement as a placeholder for future code
tasks = ["Study", "Exercise", "Cook", "Clean"]
for task in tasks:
    if task == "Cook":
        pass #Will implement cooking later
    else:
        print("Doing", task)