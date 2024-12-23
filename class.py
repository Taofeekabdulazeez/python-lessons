class Person:
    def __init__(self, name):
        self._name = name

    def introduction(self):
        return f"Hello, my name is {self._name}"
    
    @staticmethod
    def aboutClass():
        return 'This is a Person Class'


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduction(self):
        return f"Hello, my name is {self._name} and i am studying {self.course}"





person1 = Person('Taofeek')
student1 = Student('Taofeek', 'Computer Science')
print(person1.introduction())
print(student1.introduction())