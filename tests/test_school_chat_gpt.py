import pytest

from source.school import Classroom, Student, Teacher, TooManyStudents  # Adjust import as necessary

@pytest.fixture
def classroom():
    teacher = Teacher("Mr. Smith")
    students = [Student(f"Student {i}") for i in range(9)]
    return Classroom(teacher, students, "Math 101")

def test_add_student(classroom):
    new_student = Student("Student 10")
    classroom.add_student(new_student)
    assert len(classroom.students) == 10
    assert classroom.students[-1].name == "Student 10"

def test_add_student_too_many(classroom):
    classroom.add_student(Student("Student 10"))
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Student 11"))

def test_remove_student(classroom):
    classroom.remove_student("Student 0")
    assert len(classroom.students) == 8
    assert all(student.name != "Student 0" for student in classroom.students)

def test_change_teacher(classroom):
    new_teacher = Teacher("Mrs. Johnson")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Mrs. Johnson"
