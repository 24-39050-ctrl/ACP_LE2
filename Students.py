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

#Chuld class
class FinalStudent(StudentRecords, Student):
    
    #calling the parent class StudentRecords
    records = StudentRecords()

    #Adding students
    print(records.add_student("01", "Daryl Tiqio", "daryltiqio@email.com"))
    print(records.add_student("02", "Aaron Dave", "aarondave@email.com",
                              {"Math": 85, "Science": 92, "English": 88,
                                  "History": 79, "Physics": 91},
                              {"Math", "Science", "English", "History", "Physics"}))

    print(records.add_student("03", "Maria Santos", "mariasantos@email.com",
                              {"Math": 90, "Science": 94, "English": 89,
                                  "History": 95, "Physics": 94},
                              {"Math", "Science", "English", "History", "Physics"}))

    #updating studentsd
    print(records.update_student("01", email="daryltiqio@email.com"))

    #enrolling courses
    print(records.enroll_course("01", "History"))
    print(records.enroll_course("01", "Math"))
    print(records.enroll_course("01", "English"))
    print(records.enroll_course("01", "Science"))
    print(records.enroll_course("01", "Physics"))
    print(records.enroll_course("01", "Computer Programming"))
    
    print(records.update_student("01", grades={
          "History": 88, "Math": 76, "English": 82, "Science": 85, "Physics": 90, "Computer Programming": 87}))

    print(records.enroll_course("02", "Computer Programming"))
    print(records.enroll_course("02", "Physics"))
    print(records.update_student("02", grades={
          "Computer Programming": 89, "Physics": 83}))

    #searching students by id
    print("\nSearch by ID:")
    print(records.search_student("01"))
    print(records.search_student("02"))
    print(records.search_student("03"))

    #searching students  by name
    print("\nSearch by name (partial match):")
    print(records.search_by_name("Daryl"))
    print(records.search_by_name("Aaron"))
    print(records.search_by_name("Maria"))

    #printing the students id and name and their courses and gpa
    for student in records.students:
        print(f"\nGPA for {student.id_name[1]}: {student.calculate_gpa()}")
        print(f"Courses taken: {', '.join(sorted(student.courses))}\n")

    #deleting styudent 
    print(records.delete_student("02"))

    #searching the deleted student
    print(records.search_student("02"))


    
