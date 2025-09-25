'''
Calculator Program that asks user for two numbers and can decide to add, sub, mult, or div
Three Principles Used:
KISS
DRY Code
Single Responsibility 
'''


def get_number(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Invalid number. Please try again")
#Each function does its own thing
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def menu_interface():
  print("\n--- Calculator ---")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Quit")
  return input("Choose an option (1-5): ")
#Relatively Simple and nothing is repeated unnecesarily
def main():
  while True:
    choice = menu_interface()

    if choice not in ("1", "2", "3", "4"):
      print("Invalid choice. Try Again.")
      continue

    num1 = get_number("Enter your first number")
    num2 = get_number("Enter your second number")

    if choice == "1":
      result = add(num1, num2)
    elif choice == "2":
      result = subtract(num1, num2)
    elif choice == "3":
      result = multiply(num1, num2)
    elif choice == "4":
      result = divide(num1, num2)
    else:
      print("Calculator Off")
      break

    print(f"Result: {result}")

if __name__ == "__main__":
  main()





