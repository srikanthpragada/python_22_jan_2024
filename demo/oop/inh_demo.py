from abc import ABC, abstractmethod


# abstract class
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name)
        print(self.email)

    def getemail(self):
        return self.email

    @abstractmethod
    def occupation(self):
        pass


class Student(Person):
    def __init__(self, name, email, course, college):
        super().__init__(name, email)
        self.course = course
        self.college = college

    # Overriding
    def show(self):
        super().show()
        print(self.course)
        print(self.college)

    def occupation(self):
        return f"Pursuing {self.course} in {self.college}"


s = Student("Ben", 'ben@gmail.com', 'MSCS', "Standford")
s.show()
print(s.getemail())  # comes from Person
print(s.occupation())
