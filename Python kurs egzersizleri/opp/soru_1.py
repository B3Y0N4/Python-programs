class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self,course_name,max_student):
        self.course_name = course_name
        self.max_student = max_student
        self.students = []
    def add_student(self,students):
        if len(self.students) < self.max_student:
            self.students.append(students)
            return True
        return False
    def get_avrage_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Abduljalal",18,96)
s2 = Student("Oussam",21,98)
s3 = Student ("Ammar",17,85)

course1 = Course("Ruby",2)
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)
course2 = Course("Doğresul Cebri", 3)
course2.add_student(s1)
course2.add_student(s2)
course2.add_student(s3)

print (course1.students[0].name)
print (course1.students[1].name)
print (course1.get_avrage_grade())


print (course2.students[0].name)
print (course2.students[1].name)
print (course2.students[2].name)
print (course1.get_avrage_grade())
