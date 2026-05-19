balance = 5000

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        raise Exception("Insufficient balance")

except ValueError:
    print("Please enter numbers only")

except Exception as e:
    print("Error:", e)

else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

finally:
    print("Thank you for using ATM")




# Function for Addition
def add(a, b):
    return a + b


# Function for Subtraction
def sub(a, b):
    return a - b


# Function for Multiplication
def mul(a, b):
    return a * b


# Function for Division
def div(a, b):
    return a / b


# Infinite loop to run calculator continuously
while True:

    # Display menu
    print("\n--- SIMPLE CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    # Take user choice
    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == '5':
        print("Exiting calculator...")
        break

    # Check valid operation
    elif choice in ['1', '2', '3', '4']:

        try:
            # Taking user input
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            # Perform operation
            if choice == '1':
                print("Result =", add(a, b))

            elif choice == '2':
                print("Result =", sub(a, b))

            elif choice == '3':
                print("Result =", mul(a, b))

            elif choice == '4':
                print("Result =", div(a, b))

        # Handles invalid number input
        except ValueError:
            print("Error: Please enter numbers only.")

        # Handles division by zero
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

        # Executes always
        finally:
            print("Operation completed.")

    # Invalid menu choice
    
    else:
        print("Invalid choice! Please select between 1 and 5.")




# Creating Student class
class Student:

    # Constructor
    def __init__(self, name, marks):

        # Checking marks validity
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        # Instance variables
        self.name = name
        self.marks = marks

    # Method to display student details
    def display(self):
        print("\n--- STUDENT DETAILS ---")
        print("Name :", self.name)
        print("Marks:", self.marks)


# Exception handling starts here
try:

    # Taking user input
    name = input("Enter student name: ")

    # Risky code
    marks = int(input("Enter student marks: "))

    # Creating object
    s1 = Student(name, marks)

    # Calling display method
    s1.display()

# Handles invalid integer input
except ValueError as e:
    print("\nError:", e)

# Executes always
finally:
    print("\nProgram execution completed.")




from abc import ABC, abstractmethod

# Abstract Class
class ATM(ABC):

    def __init__(self, balance):

        try:
            if balance < 0:
                raise ValueError("Balance cannot be negative")

            self.__balance = balance

        except ValueError as e:
            print("Error:", e)

    def show_balance(self):

        try:
            print("Balance:", self.__balance)

        except AttributeError:
            print("Error: Invalid balance")

    @abstractmethod
    def display(self):
        pass


# Child Class
class SBIATM(ATM):

    def display(self):
        print("Welcome to SBI ATM")


# Object Creation
s = SBIATM(-500)

s.display()
s.show_balance()