import math

# ---------- Area Classes (Abstraction) ----------
class Area:
    """Abstract base class for shapes."""
    def area(self):
        pass

class Rectangle(Area):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Area):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# ---------- Bank Account (Encapsulation) ----------
class BankAccount:
    """Simple bank account with deposit/withdraw functionality."""
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# ---------- Teachers (Polymorphism) ----------
class EnglishTeacher:
    def teach(self):
        return "Teaching English grammar"

class MathTeacher:
    def teach(self):
        return "Teaching Algebra and Calculus"


# ---------- Testing Code ----------
if __name__ == "__main__":
    # Shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 5)
    print(circle.area())
    print(rectangle.area())

    # Bank account
    acc = BankAccount(100)
    acc.deposit(50)
    acc.withdraw(30)
    print(acc.get_balance())

    # Polymorphism
    teachers = [EnglishTeacher(), MathTeacher()]
    for t in teachers:
        print(t.teach())
