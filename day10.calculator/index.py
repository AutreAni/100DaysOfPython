from art import calc

print(calc)
operators = ["+", "-", "*", "/"]
def print_operators():
    for op in operators:
        print(op)
def calc_result_unsafe(x, y, operator):
    expression = f"{x} {operator}{y}"
    result = eval(expression)
    return result

def calc_result_safe(x, y, operator):
    x = float(x)
    y = float(y)
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    if operator in operations:
        return round(operations[operator](x, y),2)
    else:
        print("Invalid operator")

saved_result = None
count = 0
while True:
    if saved_result:
        first_number = saved_result
    else:
        first_number = input("What's the first number?: ")
    second_number = input("What's the second number?: ")
    if not count:
        print_operators()
    count += 1
    operator =input("Pick an operator: ")
    saved_result = calc_result_safe(first_number, second_number, operator)
    print(first_number, operator, second_number,"=",saved_result)
    y_or_n = input(f"Type 'y' to continue calculating with {saved_result}, or type 'n' to start a new calculation: ")
    if y_or_n == "n":
        saved_result = None
