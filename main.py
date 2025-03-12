def calculate(num1, num2, operation):
    if operation=="+":
        return num1 + num2
    elif operation=="-":
        return num1 - num2
    elif operation=="*":
        return num1 * num2
    elif operation=="/":
        if num2==0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalivd operation. Please enter +, -, *, or /.")
        return
    print("Result:", result)
    except ValueError
print("Invalid input. Please enter valid numbers.")


