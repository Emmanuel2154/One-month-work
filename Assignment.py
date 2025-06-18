class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")


class Student(Person):
    def __init__(self, student_id):
        self.student_id = student_id
        super().__init__("Emmanuel", 12)

    def study(self):
        print(f"Hi, I am {self.name}, a student with {self.student_id}")


class Teacher(Person):
    def __init__(self, subject):
        self.subject = subject
        super().__init__("Mr. Martin", 32)

    def teach(self):
        print(f"Hello, I am {self.name} and I teach {self.subject}")


random_person = Person("Emmanuel", 12)
random_person.introduce()

student1 = Student(101)
student1.study()

teacher1 = Teacher("Mathematics")
teacher1.teach()