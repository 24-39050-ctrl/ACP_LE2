class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)  # Tuple for ID and name
        self.email = email  # String for email
        self.grades = grades if grades is not None else {}  # Dictionary for grades
        self.courses = set(courses) if courses is not None else set()  # Set for courses
        pass
    def __str__(self):
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, "
                f"Courses: {', '.join(self.courses) if self.courses else 'None'}, "
                f"Grades: {self.grades if self.grades else 'None'}")
        pass

class StudentRecords:
    def __init__(self):
        self.students = []  # List to hold student objects
        pass

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully"
        pass
