
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    he reason for using operations[operation_symbol] instead of operation symbol is because operations is a dictionary that contains the mapping between operation symbols (e.g., '+', '-', '*', '/') and their corresponding functions (e.g., add, subtract, multiply, divide).
#When you use operations[operation_symbol], you are accessing the value associated with the key operation_symbol in the dictionary operations. In this case, operation_symbol is the user's input, which represents the chosen operation (e.g., '+'). By using square brackets with operations[operation_symbol], you can look up and retrieve the function associated with the specific operation symbol entered by the user.
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
