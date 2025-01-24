class Student:
    def __init__(self, name, age, grade, subjects):
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects
    
    def display_info(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Grade: ',self.grade)
        print('Subjects: ', self.subjects)
s = Student('manas',33,'B','mechanical')

s.display_info()