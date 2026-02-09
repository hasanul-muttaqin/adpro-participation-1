class Calculator:
    def add(self, angka1, angka2):
        return angka1 + angka2
    def subtract(self, branch, subtract):
        return branch - subtract
    def multiply(self, var1, var2):
        return var1 * var2
    def divide(self, branch, divide):
        return branch / divide
    def modulo(self, x, y):
        return x%y
    def power(self, aku, keren):
        return aku ** keren
if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Modulo: ", calc.modulo(10, 5))
    print("Power: ", calc.power(10, 5))
