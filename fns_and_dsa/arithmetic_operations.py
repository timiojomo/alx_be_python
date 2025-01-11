
def perform_operation(num1, num2, operation):  
    match operation:
        case "add":
            result = float(num1) + float(num2)
        case "subtract":
            result = float(num1) - float(num2)
        case "multiply":
            result = float(num1) * float(num2)
        case "divide":
            if num2 == 0:
                print("can't divide by zero")
            elif num2 != 0:
                result = float(num1) / float(num2)
    return result