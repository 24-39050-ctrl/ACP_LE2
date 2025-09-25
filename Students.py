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

    #calculating the gpa of studentss
     def calculate_gpa(self):
        if not self.grades:
            return 0.0

        grade_points = {
            'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0
        }

        total_points = 0
        valid_grades = 0

        for score in self.grades.values():
            if isinstance(score, (int, float)):
                if score >= 90:
                    letter_grade = 'A'
                elif score >= 80:
                    letter_grade = 'B'
                elif score >= 70:
                    letter_grade = 'C'
                elif score >= 60:
                    letter_grade = 'D'
                else:
                    letter_grade = 'F'

                if letter_grade in grade_points:
                    total_points += grade_points[letter_grade]
                    valid_grades += 1

        return round(total_points / valid_grades, 2) if valid_grades > 0 else 0.0
         

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

    #Update students
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
        
     # Remove student if found
    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.id_name[0] == student_id:
                del self.students[i]
                return "Student deleted successfully"

        return "Student not found"

    #enroll all course 
    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return "Course enrolled successfully"

        return "Student not found"

    #search the students by id
    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)

        return "Student not found"

    #search students by na,me
    def search_by_name(self, name):
        matches = []
        for student in self.students:
            if name.lower() in student.id_name[1].lower():
                matches.append(student)

        if matches:
            return "\n".join(str(student) for student in matches)
        else:
            return "No students found with that name"

    
