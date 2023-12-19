nofnof = "NöfNöf"

class KlinoffMath:
    @staticmethod
    def add(a, b):
        return print(f"{a + b}\nAdded!! {nofnof}")

    @staticmethod
    def subtract(a, b):
        return print(f"{a - b}\nSubtracted!! {nofnof}")

    @staticmethod
    def multiply(a, b):
        return print(f"{a * b}\nMultiplied!! {nofnof}")

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError(f"Division by zero is not allowed... {nofnof} I am displeased {nofnof}")
        return print(f"{a / b}\nDivided!! {nofnof}")
