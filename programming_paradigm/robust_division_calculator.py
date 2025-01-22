def safe_divide(numerator, denominator):
    try:
        numerator / denominator
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero")
        return f"The result of the division is {float(numerator / denominator)}"
    except ValueError:
        print("Error: Please enter numeric values only")
