class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_student_mark(self):
        if not self.grades:
            return 0
        else:
            all_grades = []
            for grade in self.grades.values():
                all_grades.extend(grade)
        return round(sum(all_grades) / len(all_grades), 1)

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and (course in self.finished_courses or course in self.courses_in_progress)
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {
            self.average_student_mark()}\n"
            f"Курсы в процессе изучения: {
            ", ".join(
                self.courses_in_progress)}\n"
            f"Завершённые курсы: {", ".join(self.finished_courses)}")

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_student_mark() == other.average_student_mark()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_student_mark() > other.average_student_mark()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_student_mark() >= other.average_student_mark()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_lecturer_mark()}")

    def average_lecturer_mark(self):
        if not self.grades:
            return 0
        else:
            all_grades = []
            for grade in self.grades.values():
                all_grades.extend(grade)
        return round(sum(all_grades) / len(all_grades), 1)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_lecturer_mark() == other.average_lecturer_mark()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_lecturer_mark() > other.average_lecturer_mark()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_lecturer_mark() >= other.average_lecturer_mark()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Алексей', 'Алексеевич')
reviewer_1 = Reviewer('Пётр', 'Петров')
student_1 = Student('Ольга', 'Алёхина', 'Ж')
student_2 = Student('Михаил', 'Михайлович', 'М')

student_1.courses_in_progress += ['Python', 'Java', 'C++']
student_1.finished_courses += ['Git']
student_2.courses_in_progress += ['Python', 'C++', 'Java']
student_2.finished_courses += ['Git']
lecturer_1.courses_attached += ['Python', 'C++', 'Java']
lecturer_2.courses_attached += ['Python', 'Java', 'C++']
reviewer_1.courses_attached += ['Python', 'C++', 'Java']

student_1.rate_lecture(lecturer_1, 'C++', 7)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Java', 8)
student_1.rate_lecture(lecturer_2, 'C++', 8)
student_1.rate_lecture(lecturer_2, 'Python', 6)
student_1.rate_lecture(lecturer_2, 'Java', 8)
student_2.rate_lecture(lecturer_1, 'C++', 9)
student_2.rate_lecture(lecturer_1, 'Python', 6)
student_2.rate_lecture(lecturer_1, 'Java', 6)
student_2.rate_lecture(lecturer_2, 'C++', 10)
student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Java', 6)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'C++', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Java', 7)
reviewer_1.rate_hw(student_2, 'C++', 10)

print(lecturer_1.grades)
print(lecturer_2.grades)

print(reviewer_1)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)

print(student_1 == student_2)
print(student_1 != student_2)
print(student_1 > student_2)
print(student_1 < student_2)
print(student_1 >= student_2)
print(student_1 <= student_2)

print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 >= lecturer_2)
print(lecturer_1 <= lecturer_2)
