def safe_divide(numerator: float, denominator: float):
    try:
        numerator / denominator
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero")
        return f"The result of the division is {numerator / denominator}"
    except ValueError:
        print("Error: Please enter numeric values only")
