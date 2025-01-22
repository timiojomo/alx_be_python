def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        numerator / denominator
        #if denominator == 0:
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    except ValueError:
        raise ValueError("Error: Please enter numeric values only.")
    return f"The result of the division is {numerator / denominator}"
