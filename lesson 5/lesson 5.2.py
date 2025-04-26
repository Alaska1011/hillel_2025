while True:
    print("Enter first number: ")
    num1 = float(input())

    print("Enter operation (+, -, *, /): ")
    operation = input()

    print("Enter second number: ")
    num2 = float(input())

    if operation == '+':
        result = num1 + num2
        print("result:", result)
    elif operation == '-':
        result = num1 - num2
        print("result:", result)
    elif operation == '*':
        result = num1 * num2
        print("result:", result)
    elif operation == '/':
        if num2 == 0:
            print("Error Divisor cannot be equal to 0")
        else:
            result = num1 / num2
            print("result:", result)
    else:
        print("Error Invalid operation! Try again")
    continue_calculation = input("Enter y").strip().lower()
    if continue_calculation not in ['y']:
        break

