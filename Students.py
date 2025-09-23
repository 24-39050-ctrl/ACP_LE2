class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)  # Tuple for ID and name
        self.email = email  # String for email
        self.grades = grades if grades is not None else {}  # Dictionary for grades
        self.courses = set(courses) if courses is not None else set()  # Set for courses
    def __str__(self):
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, "
                f"Courses: {', '.join(self.courses) if self.courses else 'None'}, "
                f"Grades: {self.grades if self.grades else 'None'}")

class StudentRecords:
    def __init__(self):
        self.students = []  # List to hold student objects

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                return "Student ID already exists"

        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades.update(grades)
                if courses is not None:
                    student.courses.update(courses)
                return "Student updated successfully"

        return "Student not found"

    def delete_student(self, student_id):
        # Remove student if found
        for i, student in enumerate(self.students):
            if student.id_name[0] == student_id:
                del self.students[i]
                return "Student deleted successfully"

        return "Student not found"


    
