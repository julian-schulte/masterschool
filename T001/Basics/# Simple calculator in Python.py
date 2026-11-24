# Simple calculator in Python


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter calculation (e.g. 2 + 2): ")
            if expression.strip().lower() in {"quit", "exit", "q"}:
                print("Goodbye!")
                break

            tokens = expression.split()
            if len(tokens) != 3:
                raise ValueError("Please enter a valid expression in the form: number operator number")

            left, operator, right = tokens
            left = float(left)
            right = float(right)

            if operator == "+":
                result = add(left, right)
            elif operator == "-":
                result = subtract(left, right)
            elif operator == "*":
                result = multiply(left, right)
            elif operator == "/":
                result = divide(left, right)
            else:
                raise ValueError("Unsupported operator. Use +, -, *, or /.")

            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
