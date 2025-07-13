class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Assigned {grade} to {student.name}")
                return
        print("Student not found.")

    def display_all_grades(self):
        for student in self.students:
            print(f"\nGrades for {student.name}:")
            student.display_grades()

if __name__ == "__main__":
    instructor = Instructor("Allan", "API")

    while True:
        print("\n1. Add Student\n2. Assign Grade\n3. Display All Grades\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Student Name: ")
            student_id = input("Student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)
            print(f"Student {name} added.")

        elif choice == '2':
            student_id = input("Student ID: ")
            assignment_name = input("Assignment: ")
            grade = input("Grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == '3':
            instructor.display_all_grades()

        elif choice == '4':
            break
        else:
            print("Invalid choice.")
