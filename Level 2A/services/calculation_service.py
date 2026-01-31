class CalculationService:
    @staticmethod
    def calculate(operation, x, y):
        """
        Performs a calculation based on the operation.
        Raises ValueError if operation is invalid.
        """
        if operation == "add":
            return x+y
        elif operation == "subtract":
            return x - y
        elif operation == "multiply":
            return x * y
        elif operation == "divide":
            if y == 0:
                raise ValueError("Cannot divide by zero")
            return x / y
        else:
            raise ValueError(f"Invalid operation: {operation}")
