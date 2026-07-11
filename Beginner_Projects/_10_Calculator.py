logo = r"""
 ___________________________________________
|  ________________________________  |
| |    Pythonista    0.              | |
| |________________________________| |
|                                      |
|  ___________   ___________   ___________   ________
| |   7       | |   8       | |   9       | |   +    |
| |___________| |___________| |___________| |________|
|  ___________   ___________   ___________   ________
| |   4       | |   5       | |   6       | |   -    |
| |___________| |___________| |___________| |________|
|  ___________   ___________   ___________   ________
| |   1       | |   2       | |   3       | |   x    |
| |___________| |___________| |___________| |________|
|  ___________   ___________   ___________   ________
| |   .       | |   0       | |   =       | |   /    |
| |___________| |___________| |___________| |________|
|______________________________________________|
"""
print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

num1 = 0
num1 = int(input("Enter a number: "))

while True:

    operation = input("Enter operation: ")

    num2 = int(input("Enter another number: "))

    if operation == "+":
        result = add(num1, num2)
        print(result)
    elif operation == "-":
        result = (subtract(num1, num2))
        print(result)
    elif operation == "*":
        result = multiply(num1, num2)
        print(result)
    elif operation == "/":
        result = divide(num1, num2)
        print(result)
    else:
        print("Invalid operation")


    next_operation = input(f"Type y for continue operations with {result} or n for new calculation or x for exit()\n").lower()

    if next_operation == "n":
        num1 = int(input("Enter a number: "))

    elif next_operation == "y":
        num1 = result

    elif next_operation == "x":
        break
    else:
        print("Invalid option")