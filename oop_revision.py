class Student:
    school_name = "AI Academy"  # class variable

    def __init__(self, name, marks):
        self.name = name       # instance variable
        self._marks = marks    # protected variable

    def set_marks(self, marks):
        self._marks = marks    # setter
    
    def get_marks(self):
        return self._marks     # getter
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self._marks}")

# test
s1 = Student("Rohan", 88)
s1.display()
