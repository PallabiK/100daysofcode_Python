import calc_art
print(calc_art.logo)
#calculator
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

def calculator():
  num1 = float(input("What is the 1st number?: "))
  for symbol in operations:
      print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {result}.")
    options = int(input(f"Type '1' to continue calculating with {result} or '2' to start a new calculation or '3' to exit the calculator: "))
    if  options == 1:
      num1 = result
    elif options == 2:
      should_continue = False
      calculator()
    elif options == 3:
      should_continue = False
      print("See you soon!")
    else:
      print("Invalid entry.")
      should_continue = False
      
print("Welcome to the calculator!")
calculator()