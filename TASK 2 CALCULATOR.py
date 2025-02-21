
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = input("Choose an operation (1/2/3/4) or 'q' to quit: ")

            if choice == 'q':
                print("Exiting the calculator. Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is {result}")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
if __name__ == "__main__":
    calculator()
